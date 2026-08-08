# Windows distribution

## Architecture

Phase 1 remains a Streamlit RAG application. Windows packaging adds a thin
launcher and does not change chunking, retrieval, prompts, embedding behavior,
generation behavior, or evaluation logic.

The PyInstaller build is `onedir`:

- application executable: `RAG-Finance.exe`
- bundled Python/runtime: `_internal/`
- committed seed source: `packaging/windows/resources/qdrant_local`
- bundled read-only seed vector store: `_internal/resources/qdrant_local`
- mutable runtime data: `%LOCALAPPDATA%\RAGFinance\`

Qdrant remains **local mode**. No Qdrant server and no Docker are required.

## Runtime paths

The launcher validates the bundled seed and copies it on first run to:

`%LOCALAPPDATA%\RAGFinance\vectorstore\qdrant_local`

Qdrant opens that writable copy rather than the files installed with the
application. This avoids lock/WAL writes under the installation directory.

Other writable data is also under `%LOCALAPPDATA%\RAGFinance`, including the
SQLite conversation database at `data\history.sqlite3`, diagnostic logs under
`logs\`, and Streamlit chat/cache runtime files. Upgrades and uninstall do not
remove this user data.

## API configuration

Embedding and generation still use the existing OpenAI-compatible Arvan API.
A real API secret is never committed. The private delivery workflow materializes
the repository secret as `.env` and bundles it beside `RAG-Finance.exe`, so the
trusted/internal recipient does not configure anything manually:

```env
ARVAN_AI_API_KEY=...
ARVAN_EMBEDDING_URL=...
ARVAN_CHAT_URL=...
ARVAN_CHAT_API_KEY=...
ARVAN_CHAT_MODEL=Qwen3-30B-A3B
```

The launcher loads that file at runtime. Do not commit it. Because a technical
recipient can extract client-side configuration, this build is for trusted,
internal distribution rather than public release.

## Vector store seed

The validated Phase 1 seed is committed under:

`packaging/windows/resources/qdrant_local`

Required content includes:

- `meta.json`
- `collection/financial_knowledge_base/`
- `collection/financial_knowledge_base/storage.sqlite`

The temporary root archive `qdrant_local.zip` is not part of the final tree or
artifacts. A source `.lock` is removed before the seed is committed and the
workflow fails if any `.lock` remains.

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

The build script refuses to run from another branch and validates the committed
runtime seed before invoking PyInstaller.

## GitHub Actions

Workflow: `.github/workflows/build-windows.yml`

Supported triggers include:

- manual `workflow_dispatch`
- pushes to `phase1-windows`
- the isolated validation PR from `phase1-windows` to `main`

It validates branch scope and the seed, builds the portable directory, runs an
API-independent Windows smoke test, validates bundle structure, creates
`RAG-Finance-Windows.zip`, then builds and validates the Inno Setup installer.

Artifacts:

- `RAG-Finance-Windows-Portable`
- `RAG-Finance-Windows-Installer`

## Smoke test

The client test launches the production executable and:

- occupies port 8501 and verifies automatic fallback to another loopback port
- verifies the official Streamlit health endpoint and the real root page
- confirms the browser target is exactly the healthy root URL
- confirms the bundled seed was copied to the temporary `LOCALAPPDATA`
- confirms runtime `meta.json` and `storage.sqlite` exist and are non-empty
- runs a real embedding, retrieval, and generation request inside the packaged EXE
- persists the successful Q&A in SQLite and verifies it after an app restart

The final client validation requires Internet access and the valid API
configuration materialized from `RAG_FINANCE_ENV`.

## Installer

Inno Setup script:

`packaging/windows/installer.iss`

Output:

`RAG-Finance-Setup.exe`

The installer is a per-user installation under:

`%LOCALAPPDATA%\Programs\RAG Finance`

It does not require elevation, creates a Start Menu shortcut, offers an optional
Desktop shortcut, and includes standard uninstall support. CI performs silent
install, installed-EXE smoke testing, and silent uninstall where supported by
the hosted Windows runner.

## Troubleshooting

If the launcher reports missing API configuration, create the real `.env`
beside the executable.

If it reports a missing vector store, confirm the package contains
`_internal/resources/qdrant_local` and rebuild from the validated seed.

If Windows SmartScreen or antivirus warns about the executable, note that
unsigned PyInstaller applications can trigger reputation-based warnings.
Production code signing requires a legitimate signing certificate; a self-signed
certificate is not a production substitute.
