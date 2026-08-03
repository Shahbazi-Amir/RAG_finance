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
New-Item -ItemType Directory -Force -Path $LocalAppData | Out-Null

$env:LOCALAPPDATA = $LocalAppData
$env:RAG_FINANCE_SKIP_CONFIG_CHECK = "1"
$env:RAG_FINANCE_PORT = "$Port"
$env:ARVAN_AI_API_KEY = "smoke-test"
$env:ARVAN_EMBEDDING_URL = "http://127.0.0.1:9/v1"
$env:ARVAN_CHAT_URL = "http://127.0.0.1:9/v1"
$env:ARVAN_CHAT_API_KEY = "smoke-test"
Remove-Item Env:RAG_FINANCE_VECTORSTORE_PATH -ErrorAction SilentlyContinue

$process = Start-Process -FilePath $ExePath -PassThru
try {
    $deadline = (Get-Date).AddSeconds(90)
    $ready = $false

    while ((Get-Date) -lt $deadline) {
        if ($process.HasExited) {
            throw "Executable exited early with code $($process.ExitCode)."
        }

        try {
            $response = Invoke-WebRequest `
                -Uri "http://127.0.0.1:$Port" `
                -UseBasicParsing `
                -TimeoutSec 2
            if ($response.StatusCode -ge 200 -and $response.StatusCode -lt 500) {
                $ready = $true
                break
            }
        }
        catch {
            Start-Sleep -Milliseconds 500
        }
    }

    if (-not $ready) {
        throw "Streamlit did not become ready on localhost:$Port."
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
    if (-not $process.HasExited) {
        Stop-Process -Id $process.Id -Force
    }
    Start-Sleep -Milliseconds 500
    if (Test-Path $TempRoot) {
        Remove-Item -Path $TempRoot -Recurse -Force -ErrorAction SilentlyContinue
    }
}
