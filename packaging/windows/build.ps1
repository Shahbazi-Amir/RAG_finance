param(
    [switch]$SkipVectorStoreCheck
)

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $RepoRoot

$branch = (git branch --show-current).Trim()
if ($branch -ne "phase1-windows") {
    throw "Refusing Windows packaging from branch '$branch'. Expected phase1-windows."
}

$VectorStore = Join-Path $RepoRoot "data\vectorstore\qdrant_local"
if (-not $SkipVectorStoreCheck -and -not (Test-Path $VectorStore)) {
    throw "Runtime vector store is missing: data/vectorstore/qdrant_local"
}

python -m PyInstaller --noconfirm --clean "packaging\windows\rag_finance.spec"

$Portable = Join-Path $RepoRoot "dist\RAG-Finance"
Copy-Item ".env.example" (Join-Path $Portable ".env.example") -Force
Copy-Item "README-WINDOWS.txt" (Join-Path $Portable "README-WINDOWS.txt") -Force

$Exe = Join-Path $Portable "RAG-Finance.exe"
if (-not (Test-Path $Exe)) {
    throw "RAG-Finance.exe was not created."
}

Write-Host "Portable build ready at $Portable"
