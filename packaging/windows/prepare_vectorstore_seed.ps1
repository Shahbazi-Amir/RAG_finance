param(
    [switch]$CommitSeed
)

$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
Set-Location $RepoRoot

$branch = $env:GITHUB_HEAD_REF
if ([string]::IsNullOrWhiteSpace($branch)) {
    $branch = (git branch --show-current).Trim()
}
if ($branch -ne "phase1-windows") {
    throw "Refusing vector store preparation from branch '$branch'. Expected phase1-windows."
}

$ZipPath = Join-Path $RepoRoot "qdrant_local.zip"
$SeedRoot = Join-Path $RepoRoot "packaging\windows\resources\qdrant_local"
$MetaPath = Join-Path $SeedRoot "meta.json"
$CollectionPath = Join-Path $SeedRoot "collection\financial_knowledge_base"
$StoragePath = Join-Path $CollectionPath "storage.sqlite"

function Assert-Seed {
    if (-not (Test-Path $SeedRoot -PathType Container)) {
        throw "Vector store seed directory is missing: $SeedRoot"
    }
    if (-not (Test-Path $MetaPath -PathType Leaf)) {
        throw "Vector store meta.json is missing: $MetaPath"
    }
    if (-not (Test-Path $CollectionPath -PathType Container)) {
        throw "Vector store collection is missing: $CollectionPath"
    }
    if (-not (Test-Path $StoragePath -PathType Leaf)) {
        throw "Vector store storage.sqlite is missing: $StoragePath"
    }

    $locks = @(Get-ChildItem -Path $SeedRoot -Force -Recurse -File -Filter ".lock" -ErrorAction SilentlyContinue)
    if ($locks.Count -gt 0) {
        throw "Vector store seed contains a forbidden .lock file: $($locks[0].FullName)"
    }

    if ((Get-Item $StoragePath).Length -le 0) {
        throw "Vector store storage.sqlite is empty."
    }
}

if (Test-Path $ZipPath -PathType Leaf) {
    $ExtractRoot = Join-Path $env:RUNNER_TEMP ("rag-finance-vector-seed-" + [guid]::NewGuid().ToString("N"))
    New-Item -ItemType Directory -Force -Path $ExtractRoot | Out-Null

    try {
        Expand-Archive -LiteralPath $ZipPath -DestinationPath $ExtractRoot -Force

        $candidate = $null
        $metaFiles = @(Get-ChildItem -Path $ExtractRoot -Recurse -Force -File -Filter "meta.json")
        foreach ($meta in $metaFiles) {
            $root = $meta.Directory.FullName
            $storage = Join-Path $root "collection\financial_knowledge_base\storage.sqlite"
            if (Test-Path $storage -PathType Leaf) {
                $candidate = $root
                break
            }
        }

        if (-not $candidate) {
            throw "qdrant_local.zip does not contain a valid financial_knowledge_base seed."
        }

        if (Test-Path $SeedRoot) {
            Remove-Item -Path $SeedRoot -Recurse -Force
        }
        New-Item -ItemType Directory -Force -Path (Split-Path $SeedRoot -Parent) | Out-Null
        Copy-Item -Path (Join-Path $candidate "*") -Destination $SeedRoot -Recurse -Force

        Get-ChildItem -Path $SeedRoot -Recurse -Force -File -Filter ".lock" -ErrorAction SilentlyContinue |
            Remove-Item -Force

        Assert-Seed

        Remove-Item -LiteralPath $ZipPath -Force
        if (Test-Path $ZipPath) {
            throw "Temporary qdrant_local.zip was not deleted."
        }
    }
    finally {
        if (Test-Path $ExtractRoot) {
            Remove-Item -Path $ExtractRoot -Recurse -Force
        }
    }
}
else {
    Assert-Seed
}

Write-Host "Vector store seed validated: $SeedRoot"
Write-Host "storage.sqlite bytes: $((Get-Item $StoragePath).Length)"
Write-Host "Temporary ZIP present after preparation: $(Test-Path $ZipPath)"

if ($CommitSeed) {
    if ("${env:GITHUB_EVENT_NAME}" -ne "push") {
        throw "CommitSeed is allowed only for a push workflow on phase1-windows."
    }

    git config user.name "github-actions[bot]"
    git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

    git add -f -- "packaging/windows/resources/qdrant_local"
    git add -- ".gitignore"
    git add -u -- "qdrant_local.zip"

    Write-Host "Staged seed changes:"
    git status --short

    if (Test-Path $ZipPath) {
        throw "Temporary qdrant_local.zip still exists before commit."
    }

    git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Host "No vector seed changes need committing."
        exit 0
    }

    git commit -m "add Phase 1 vector store seed for Windows distribution"
    git push origin HEAD:phase1-windows
}
