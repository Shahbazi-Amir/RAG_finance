param(
    [switch]$SkipVectorStoreCheck
)

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $RepoRoot

$branch = $env:GITHUB_HEAD_REF
if ([string]::IsNullOrWhiteSpace($branch)) {
    $branch = (git branch --show-current).Trim()
}
if ($branch -ne "phase1-windows") {
    throw "Refusing Windows packaging from branch '$branch'. Expected phase1-windows."
}

$VectorStore = Join-Path $RepoRoot "packaging\windows\resources\qdrant_local"
$Meta = Join-Path $VectorStore "meta.json"
$Collection = Join-Path $VectorStore "collection\financial_knowledge_base"
$Storage = Join-Path $Collection "storage.sqlite"

if (-not $SkipVectorStoreCheck) {
    foreach ($required in @($VectorStore, $Meta, $Collection, $Storage)) {
        if (-not (Test-Path $required)) {
            throw "Runtime vector store seed is missing: $required"
        }
    }

    $locks = @(Get-ChildItem -Path $VectorStore -Recurse -Force -File -Filter ".lock" -ErrorAction SilentlyContinue)
    if ($locks.Count -gt 0) {
        throw "Runtime vector store seed contains forbidden .lock file: $($locks[0].FullName)"
    }
}

python -m PyInstaller --noconfirm --clean "packaging\windows\rag_finance.spec"

$Portable = Join-Path $RepoRoot "dist\RAG-Finance"
if (-not (Test-Path ".env" -PathType Leaf)) {
    throw "Runtime .env was not materialized before packaging."
}
Copy-Item ".env" (Join-Path $Portable ".env") -Force
Copy-Item ".env.example" (Join-Path $Portable ".env.example") -Force
Copy-Item "README-WINDOWS.txt" (Join-Path $Portable "README-WINDOWS.txt") -Force

$Exe = Join-Path $Portable "RAG-Finance.exe"
if (-not (Test-Path $Exe)) {
    throw "RAG-Finance.exe was not created."
}

Write-Host "Portable build ready at $Portable"
