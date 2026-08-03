# Windows distribution

## Architecture

Phase 1 remains a Streamlit RAG application. Windows packaging adds a thin
launcher and does not change chunking, retrieval, prompts, embedding behavior,
generation behavior, or evaluation logic.

The PyInstaller build is `onedir`:

- application executable: `RAG-Finance.exe`
- bundled Python/runtime: `_internal/`
- bundled read-only seed vector store: `_internal/data/vectorstore/qdrant_local`
- mutable runtime data: `%LOCALAPPDATA%\RAGFinance\`

Qdrant remains **local mode**. No Qdrant server and no Docker are required.

## Runtime paths

The launcher copies the bundled Qdrant seed to:

`%LOCALAPPDATA%\RAGFinance\vectorstore\qdrant_local`

on first run. This is intentional because Qdrant local mode can create locks
and other writable state and an Installer may place application resources under
`Program Files`.

Other writable data is also under `%LOCALAPPDATA%\RAGFinance`, including the
SQLite conversation database and Streamlit chat/cache runtime files.

## API configuration

Embedding and generation still use the existing OpenAI-compatible Arvan API.
A real API secret is not committed or embedded in the public CI artifact.

For final delivery, create a private `.env` next to `RAG-Finance.exe`:

```env
ARVAN_AI_API_KEY=...
ARVAN_EMBEDDING_URL=...
ARVAN_CHAT_URL=...
ARVAN_CHAT_API_KEY=...
ARVAN_CHAT_MODEL=Qwen3-30B-A3B
```

The launcher loads that file at runtime. Do not commit it.

## Required runtime seed

A production build requires:

`data/vectorstore/qdrant_local`

to be present in the checkout before PyInstaller runs. The current repository
ignores `data/vectorstore/`; therefore CI must not publish a "successful"
portable package when that seed is absent.

The workflow intentionally fails early if this directory is missing. Supply the
validated Phase 1 vector store to the branch or restore it securely in CI before
removing that guard.

## Local Windows build

From `phase1-windows`:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-build.txt
.\packaging\windows\build.ps1
```

The build script refuses to run from another branch and refuses a production
build without the runtime vector store.

## GitHub Actions

Workflow: `.github/workflows/build-windows.yml`

Triggers:

- manual `workflow_dispatch`
- pushes to `phase1-windows`

It validates the branch and runtime seed, builds the portable directory, runs
an API-independent localhost smoke test, validates bundle structure, creates
`RAG-Finance-Windows.zip`, then builds and smoke-tests the Inno Setup installer.

Artifacts:

- `RAG-Finance-Windows-Portable`
- `RAG-Finance-Windows-Installer`

## Smoke test

The smoke test uses dummy API values and a temporary empty Qdrant local path.
It verifies only boot behavior:

- executable starts
- Streamlit starts
- localhost responds
- process does not immediately exit

It deliberately does not issue a RAG query and does not require a real API key.

## Installer

Inno Setup script:

`packaging/windows/installer.iss`

Output:

`RAG-Finance-Setup.exe`

The installer creates a Start Menu shortcut and offers an optional Desktop
shortcut. Standard uninstall support is provided by Inno Setup.

## Troubleshooting

If the launcher reports missing API configuration, create the real `.env`
beside the executable.

If it reports a missing vector store, the package was built without the Phase 1
Qdrant seed and must be rebuilt.

If Windows SmartScreen or antivirus warns about the executable, note that
unsigned PyInstaller applications can trigger reputation-based warnings.
Production code signing requires a legitimate signing certificate; a self-signed
certificate is not a production substitute.
