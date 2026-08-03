param(
    [Parameter(Mandatory = $true)]
    [string]$ExePath,
    [int]$Port = 8501
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $ExePath)) {
    throw "Executable not found: $ExePath"
}

$TempRoot = Join-Path $env:RUNNER_TEMP ("rag-finance-smoke-" + [guid]::NewGuid().ToString("N"))
$LocalAppData = Join-Path $TempRoot "LocalAppData"
$StartupError = Join-Path $TempRoot "startup-error.txt"
New-Item -ItemType Directory -Force -Path $LocalAppData | Out-Null

$env:LOCALAPPDATA = $LocalAppData
$env:RAG_FINANCE_SKIP_CONFIG_CHECK = "1"
$env:RAG_FINANCE_PORT = "$Port"
$env:RAG_FINANCE_DISABLE_BROWSER = "1"
$env:RAG_FINANCE_HEADLESS_ERRORS = "1"
$env:RAG_FINANCE_STARTUP_ERROR_FILE = $StartupError
$env:ARVAN_AI_API_KEY = "smoke-test"
$env:ARVAN_EMBEDDING_URL = "http://127.0.0.1:9/v1"
$env:ARVAN_CHAT_URL = "http://127.0.0.1:9/v1"
$env:ARVAN_CHAT_API_KEY = "smoke-test"
Remove-Item Env:RAG_FINANCE_VECTORSTORE_PATH -ErrorAction SilentlyContinue

Write-Host "Smoke-test LOCALAPPDATA: $LocalAppData"

$client = [System.Net.Http.HttpClient]::new()
$client.Timeout = [TimeSpan]::FromSeconds(2)
$process = Start-Process -FilePath $ExePath -PassThru

try {
    $deadline = (Get-Date).AddSeconds(90)
    $ready = $false
    $lastHealthError = $null
    $healthUrl = "http://127.0.0.1:$Port/_stcore/health"

    while ((Get-Date) -lt $deadline) {
        if ($process.HasExited) {
            $detail = ""
            if (Test-Path $StartupError) {
                $detail = (Get-Content $StartupError -Raw).Trim()
            }
            if ($detail) {
                throw "Executable exited early with code $($process.ExitCode): $detail"
            }
            throw "Executable exited early with code $($process.ExitCode)."
        }

        try {
            $response = $client.GetAsync($healthUrl).GetAwaiter().GetResult()
            $status = [int]$response.StatusCode
            if ($status -ge 200 -and $status -lt 500) {
                $ready = $true
                break
            }
            $lastHealthError = "HTTP status $status"
        }
        catch {
            $lastHealthError = $_.Exception.Message
        }

        Start-Sleep -Milliseconds 500
    }

    if (-not $ready) {
        $detail = ""
        if (Test-Path $StartupError) {
            $detail = (Get-Content $StartupError -Raw).Trim()
        }
        if ($detail) {
            throw "Streamlit did not become ready on $healthUrl. Startup error: $detail"
        }
        throw "Streamlit did not become ready on $healthUrl. Last health error: $lastHealthError"
    }

    $RuntimeSeed = Join-Path $LocalAppData "RAGFinance\vectorstore\qdrant_local"
    $RuntimeMeta = Join-Path $RuntimeSeed "meta.json"
    $RuntimeStorage = Join-Path $RuntimeSeed "collection\financial_knowledge_base\storage.sqlite"

    if (-not (Test-Path $RuntimeMeta -PathType Leaf)) {
        throw "Runtime vector store meta.json was not copied to LOCALAPPDATA."
    }
    if (-not (Test-Path $RuntimeStorage -PathType Leaf)) {
        throw "Runtime vector store storage.sqlite was not copied to LOCALAPPDATA."
    }
    if ((Get-Item $RuntimeStorage).Length -le 0) {
        throw "Runtime vector store storage.sqlite is empty."
    }

    Write-Host "Windows executable smoke test passed."
    Write-Host "Runtime vector store: $RuntimeSeed"
}
finally {
    $client.Dispose()

    if (-not $process.HasExited) {
        try {
            & taskkill.exe /PID $process.Id /T /F | Out-Null
        }
        catch {
            Stop-Process -Id $process.Id -Force -ErrorAction SilentlyContinue
        }
    }

    $deadline = (Get-Date).AddSeconds(10)
    while (-not $process.HasExited -and (Get-Date) -lt $deadline) {
        Start-Sleep -Milliseconds 200
        $process.Refresh()
    }

    Start-Sleep -Milliseconds 500
    try {
        if (Test-Path $TempRoot) {
            Remove-Item -Path $TempRoot -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
    catch {
        Write-Host "Smoke-test temp cleanup skipped: $($_.Exception.Message)"
    }
}
