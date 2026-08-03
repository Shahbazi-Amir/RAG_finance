from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve()
seed = root / "_internal" / "resources" / "qdrant_local"
required = [
    root / "RAG-Finance.exe",
    root / "_internal" / "app.py",
    seed / "meta.json",
    seed / "collection" / "financial_knowledge_base",
    seed / "collection" / "financial_knowledge_base" / "storage.sqlite",
    root / ".env.example",
    root / "README-WINDOWS.txt",
]
missing = [str(path) for path in required if not path.exists()]
if missing:
    raise SystemExit("Missing portable runtime files:\n" + "\n".join(missing))

storage = seed / "collection" / "financial_knowledge_base" / "storage.sqlite"
if storage.stat().st_size <= 0:
    raise SystemExit("Bundled storage.sqlite is empty.")

locks = list(seed.rglob(".lock"))
if locks:
    raise SystemExit("Bundled vector store contains forbidden .lock: " + str(locks[0]))

archives = list(root.rglob("qdrant_local.zip"))
if archives:
    raise SystemExit("Temporary qdrant_local.zip leaked into portable artifact: " + str(archives[0]))

print("Portable structure validation passed.")
print(f"Bundled storage.sqlite bytes: {storage.stat().st_size}")
