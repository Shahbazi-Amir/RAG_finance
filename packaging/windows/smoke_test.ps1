param(
    [Parameter(Mandatory = $true)]
    [string]$ExePath,
    [ValidateRange(1, 600)]
    [int]$StartupTimeoutSeconds = 120,
    [switch]$OccupyPreferredPort,
    [switch]$RunRealRag
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $ExePath)) {
    throw "Executable not found: $ExePath"
}

$TempRoot = Join-Path $env:RUNNER_TEMP ("rag-finance-smoke-" + [guid]::NewGuid().ToString("N"))
$LocalAppData = Join-Path $TempRoot "LocalAppData"
$DataRoot = Join-Path $LocalAppData "RAGFinance"
$StateFile = Join-Path $DataRoot "runtime\launch-state.json"
$BrowserUrlFile = Join-Path $DataRoot "runtime\browser-url.txt"
$StartupError = Join-Path $TempRoot "startup-error.txt"
$StartupTrace = Join-Path $TempRoot "startup-trace.txt"
$E2eResult = Join-Path $TempRoot "e2e-result.json"
$HistoryDatabase = Join-Path $DataRoot "data\history.sqlite3"
New-Item -ItemType Directory -Force -Path $LocalAppData | Out-Null

$OriginalEnvironment = @{}
foreach ($name in @(
    "LOCALAPPDATA",
    "RAG_FINANCE_DISABLE_BROWSER",
    "RAG_FINANCE_HEADLESS_ERRORS",
    "RAG_FINANCE_STARTUP_ERROR_FILE",
    "RAG_FINANCE_STARTUP_TRACE_FILE",
    "RAG_FINANCE_PORT",
    "RAG_FINANCE_VECTORSTORE_PATH",
    "RAG_FINANCE_E2E_RESULT_FILE"
)) {
    $OriginalEnvironment[$name] = [Environment]::GetEnvironmentVariable($name, "Process")
}

$env:LOCALAPPDATA = $LocalAppData
$env:RAG_FINANCE_DISABLE_BROWSER = "1"
$env:RAG_FINANCE_HEADLESS_ERRORS = "1"
$env:RAG_FINANCE_STARTUP_ERROR_FILE = $StartupError
$env:RAG_FINANCE_STARTUP_TRACE_FILE = $StartupTrace
# Regression guard: production must ignore an unrelated inherited override.
$env:RAG_FINANCE_PORT = "3000"
Remove-Item Env:RAG_FINANCE_VECTORSTORE_PATH -ErrorAction SilentlyContinue

function Stop-Application([System.Diagnostics.Process]$Process) {
    if ($null -ne $Process -and -not $Process.HasExited) {
        try { & taskkill.exe /PID $Process.Id /T /F | Out-Null }
        catch { Stop-Process -Id $Process.Id -Force -ErrorAction SilentlyContinue }
    }
}

function Wait-ForReady([System.Diagnostics.Process]$Process) {
    $deadline = (Get-Date).AddSeconds($StartupTimeoutSeconds)
    $lastError = "state file not available"
    while ((Get-Date) -lt $deadline) {
        if ($Process.HasExited) {
            $detail = if (Test-Path $StartupError) { (Get-Content $StartupError -Raw).Trim() } else { "" }
            throw "Executable exited early with code $($Process.ExitCode): $detail"
        }
        if (Test-Path $StateFile) {
            try {
                $state = Get-Content $StateFile -Raw | ConvertFrom-Json
                if ($state.status -eq "ready") {
                    $client = [System.Net.Http.HttpClient]::new()
                    try {
                        $health = $client.GetStringAsync($state.health_url).GetAwaiter().GetResult().Trim()
                        $rootResponse = $client.GetAsync($state.root_url).GetAwaiter().GetResult()
                        $rootBody = $rootResponse.Content.ReadAsStringAsync().GetAwaiter().GetResult()
                        if ([int]$rootResponse.StatusCode -ne 200) { throw "Root returned $([int]$rootResponse.StatusCode)." }
                        if ($health -ne "ok") { throw "Unexpected Streamlit health body." }
                        if ($rootBody -match "(?i)not found" -or $rootBody -notmatch "(?i)streamlit") {
                            throw "Root is not the Streamlit application page."
                        }
                        if ((Get-Content $BrowserUrlFile -Raw).Trim() -ne $state.root_url) {
                            throw "Browser target does not match the healthy root URL."
                        }
                        return $state
                    }
                    finally { $client.Dispose() }
                }
                $lastError = "launcher status: $($state.status)"
            }
            catch { $lastError = $_.Exception.Message }
        }
        Start-Sleep -Milliseconds 400
    }

    if (Test-Path $StartupTrace) {
        Write-Host "----- Launcher startup trace -----"
        Get-Content $StartupTrace
        Write-Host "----- End launcher startup trace -----"
    }
    if (Test-Path $StateFile) {
        Write-Host "----- Launcher state -----"
        Get-Content $StateFile
        $diagnosticState = Get-Content $StateFile -Raw | ConvertFrom-Json
        if ([int]$diagnosticState.selected_port -gt 0) {
            Get-NetTCPConnection -LocalPort ([int]$diagnosticState.selected_port) -ErrorAction SilentlyContinue |
                Format-Table -AutoSize LocalAddress, LocalPort, State, OwningProcess
        }
        Write-Host "----- End launcher state -----"
    }
    if (Test-Path $StartupError) {
        Write-Host "----- Launcher startup error -----"
        Get-Content $StartupError
        Write-Host "----- End launcher startup error -----"
    }
    $launcherLog = Join-Path $DataRoot "logs\launcher.log"
    if (Test-Path $launcherLog) {
        Write-Host "----- Launcher log -----"
        Get-Content $launcherLog
        Write-Host "----- End launcher log -----"
    }
    throw "Application did not become ready: $lastError"
}

function Get-HistoryCount {
    if (-not (Test-Path $HistoryDatabase)) { return 0 }
    $value = & python -c "import sqlite3,sys; c=sqlite3.connect(sys.argv[1]); print(c.execute('select count(*) from conversations').fetchone()[0]); c.close()" $HistoryDatabase
    return [int]$value
}

$listener = $null
$process = $null
$restart = $null
try {
    if ($OccupyPreferredPort) {
        $listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, 8501)
        $listener.Start()
    }
    if ($RunRealRag) { $env:RAG_FINANCE_E2E_RESULT_FILE = $E2eResult }

    $process = Start-Process -FilePath $ExePath -PassThru
    $state = Wait-ForReady $process
    if ($OccupyPreferredPort -and [int]$state.selected_port -eq 8501) {
        throw "Launcher selected the occupied preferred port."
    }
    if ([int]$state.selected_port -eq 3000) {
        throw "Launcher honored the forbidden inherited RAG_FINANCE_PORT override."
    }
    if ($listener) { $listener.Stop(); $listener = $null }

    $RuntimeSeed = Join-Path $DataRoot "vectorstore\qdrant_local"
    foreach ($required in @(
        (Join-Path $RuntimeSeed "meta.json"),
        (Join-Path $RuntimeSeed "collection\financial_knowledge_base\storage.sqlite")
    )) {
        if (-not (Test-Path $required -PathType Leaf) -or (Get-Item $required).Length -le 0) {
            throw "Runtime vector store file is missing or empty: $required"
        }
    }

    if ($RunRealRag) {
        $deadline = (Get-Date).AddSeconds(240)
        while (-not (Test-Path $E2eResult) -and (Get-Date) -lt $deadline) { Start-Sleep -Seconds 1 }
        if (-not (Test-Path $E2eResult)) { throw "Packaged real RAG test did not finish." }
        $result = Get-Content $E2eResult -Raw | ConvertFrom-Json
        if ($result.status -eq "FAIL" -or -not $result.answer_non_empty -or [int]$result.retrieved_chunks -le 0) {
            throw "Packaged real RAG test failed: $($result.error_type)"
        }
        $beforeRestart = Get-HistoryCount
        if ($beforeRestart -lt 1) { throw "Successful Q&A was not persisted to SQLite history." }

        Stop-Application $process
        $process = $null
        Remove-Item Env:RAG_FINANCE_E2E_RESULT_FILE -ErrorAction SilentlyContinue
        Remove-Item $StateFile, $BrowserUrlFile -Force -ErrorAction SilentlyContinue

        $restart = Start-Process -FilePath $ExePath -PassThru
        $restartState = Wait-ForReady $restart
        $afterRestart = Get-HistoryCount
        if ($afterRestart -ne $beforeRestart) { throw "History did not survive application restart." }
        Write-Host "History restart persistence: PASS ($afterRestart row(s))"
    }

    Write-Host "Selected port: $($state.selected_port)"
    Write-Host "Root URL: $($state.root_url)"
    Write-Host "Root 200 and Streamlit page: PASS"
    Write-Host "Browser target matches root: PASS"
    Write-Host "Windows executable client test: PASS"
}
finally {
    if ($listener) { $listener.Stop() }
    Stop-Application $process
    Stop-Application $restart
    foreach ($name in $OriginalEnvironment.Keys) {
        [Environment]::SetEnvironmentVariable($name, $OriginalEnvironment[$name], "Process")
    }
    Start-Sleep -Milliseconds 500
    Remove-Item -Path $TempRoot -Recurse -Force -ErrorAction SilentlyContinue
}
