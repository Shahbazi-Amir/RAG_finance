param(
    [Parameter(Mandatory = $true)]
    [string]$ExePath,
    [int]$Port = 8501
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $ExePath)) {
    throw "Executable not found: $ExePath"
}

$TempRoot = Join-Path $env:RUNNER_TEMP "rag-finance-smoke"
$VectorRoot = Join-Path $TempRoot "vectorstore"
$QdrantPath = Join-Path $VectorRoot "qdrant_local"
New-Item -ItemType Directory -Force -Path $QdrantPath | Out-Null

$env:RAG_FINANCE_SKIP_CONFIG_CHECK = "1"
$env:RAG_FINANCE_VECTORSTORE_PATH = $VectorRoot
$env:RAG_FINANCE_PORT = "$Port"
$env:ARVAN_AI_API_KEY = "smoke-test"
$env:ARVAN_EMBEDDING_URL = "http://127.0.0.1:9/v1"
$env:ARVAN_CHAT_URL = "http://127.0.0.1:9/v1"
$env:ARVAN_CHAT_API_KEY = "smoke-test"

$process = Start-Process -FilePath $ExePath -PassThru
try {
    $deadline = (Get-Date).AddSeconds(60)
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

    Write-Host "Windows executable smoke test passed."
}
finally {
    if (-not $process.HasExited) {
        Stop-Process -Id $process.Id -Force
    }
}
