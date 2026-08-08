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
    root / ".env",
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

env_text = (root / ".env").read_text(encoding="utf-8")
required_keys = {"ARVAN_AI_API_KEY", "ARVAN_EMBEDDING_URL", "ARVAN_CHAT_URL"}
present_keys = {
    line.split("=", 1)[0].strip()
    for line in env_text.splitlines()
    if "=" in line and not line.lstrip().startswith("#")
}
missing_keys = sorted(required_keys - present_keys)
if missing_keys:
    raise SystemExit("Bundled runtime config is missing key names: " + ", ".join(missing_keys))

forbidden_keys = {
    "GITHUB_TOKEN",
    "GH_TOKEN",
    "ACTIONS_RUNTIME_TOKEN",
    "ACTIONS_ID_TOKEN_REQUEST_TOKEN",
}
leaked_keys = sorted(forbidden_keys & present_keys)
if leaked_keys:
    raise SystemExit("Forbidden CI credential key leaked into bundle: " + ", ".join(leaked_keys))

print("Portable structure validation passed.")
print("Bundled runtime config validation passed.")
print(f"Bundled storage.sqlite bytes: {storage.stat().st_size}")
