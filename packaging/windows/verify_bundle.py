from pathlib import Path
import sys

root = Path(sys.argv[1]).resolve()
required = [
    root / "RAG-Finance.exe",
    root / "_internal" / "app.py",
    root / "_internal" / "data" / "vectorstore" / "qdrant_local",
    root / ".env.example",
    root / "README-WINDOWS.txt",
]
missing = [str(path) for path in required if not path.exists()]
if missing:
    raise SystemExit("Missing portable runtime files:\n" + "\n".join(missing))
print("Portable structure validation passed.")
