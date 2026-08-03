# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.hooks import (
    collect_data_files,
    collect_submodules,
    copy_metadata,
)


ROOT = Path(SPECPATH).resolve().parents[1]

datas = [
    (str(ROOT / "app.py"), "."),
    (str(ROOT / "data" / "cache" / "rag_cache.json"), "data/cache"),
    (str(ROOT / "data" / "vectorstore"), "data/vectorstore"),
]

datas += collect_data_files("streamlit")
datas += copy_metadata("streamlit")
datas += copy_metadata("openai")
datas += copy_metadata("qdrant-client")

hiddenimports = []
hiddenimports += collect_submodules("streamlit")
hiddenimports += collect_submodules("openai")
hiddenimports += collect_submodules("qdrant_client")
hiddenimports += [
    "config.settings",
    "src.cache.rag_cache",
    "src.database.database",
    "src.embeddings.arvan_embedder",
    "src.generation.arvan_generator",
    "src.pipeline.rag_pipeline",
    "src.retrieval.qdrant_retriever",
]

a = Analysis(
    [str(ROOT / "packaging" / "windows" / "launcher.py")],
    pathex=[str(ROOT)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="RAG-Finance",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="RAG-Finance",
)
