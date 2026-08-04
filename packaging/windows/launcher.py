from __future__ import annotations

import os
import shutil
import socket
import sys
import threading
import time
import urllib.request
import webbrowser
import faulthandler
from pathlib import Path

from dotenv import load_dotenv


APP_NAME = "RAGFinance"
DEFAULT_PORT = 8501
COLLECTION_NAME = "financial_knowledge_base"


def resource_root() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS).resolve()
    return Path(__file__).resolve().parents[2]


def executable_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return resource_root()


def writable_root() -> Path:
    if os.name == "nt":
        base = Path(os.getenv("LOCALAPPDATA") or (Path.home() / "AppData" / "Local"))
    else:
        base = Path(os.getenv("XDG_DATA_HOME") or (Path.home() / ".local" / "share"))
    path = base / APP_NAME
    path.mkdir(parents=True, exist_ok=True)
    return path


def show_error(title: str, message: str) -> None:
    if os.getenv("RAG_FINANCE_HEADLESS_ERRORS") == "1":
        print(f"{title}: {message}", file=sys.stderr)
        return

    if os.name == "nt":
        try:
            import ctypes

            ctypes.windll.user32.MessageBoxW(0, message, title, 0x10)
            return
        except Exception:
            pass
    print(f"{title}: {message}", file=sys.stderr)


def load_runtime_config(exe_root: Path, data_root: Path) -> None:
    load_dotenv(exe_root / ".env", override=False)
    load_dotenv(data_root / ".env", override=False)


def validate_api_config() -> None:
    if os.getenv("RAG_FINANCE_SKIP_CONFIG_CHECK") == "1":
        return

    required = ["ARVAN_AI_API_KEY", "ARVAN_EMBEDDING_URL", "ARVAN_CHAT_URL"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        names = ", ".join(missing)
        raise RuntimeError(
            "تنظیمات API کامل نیست. فایل .env را کنار RAG-Finance.exe قرار دهید. "
            f"مقادیر لازم: {names}"
        )


def sync_file(source: Path, target: Path) -> None:
    if not source.exists():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists() or source.read_bytes() != target.read_bytes():
        shutil.copy2(source, target)


def prepare_runtime_files(bundle: Path, data_root: Path) -> Path:
    runtime_root = data_root / "runtime"
    runtime_root.mkdir(parents=True, exist_ok=True)

    source_app = bundle / "app.py"
    if not source_app.exists():
        raise FileNotFoundError(f"Bundled app.py not found: {source_app}")

    runtime_app = runtime_root / "app.py"
    sync_file(source_app, runtime_app)

    seed_cache = bundle / "data" / "cache" / "rag_cache.json"
    runtime_cache = runtime_root / "data" / "cache" / "rag_cache.json"
    if seed_cache.exists() and not runtime_cache.exists():
        runtime_cache.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(seed_cache, runtime_cache)

    return runtime_app


def validate_vectorstore_seed(seed: Path) -> None:
    required = [
        seed / "meta.json",
        seed / "collection" / COLLECTION_NAME,
        seed / "collection" / COLLECTION_NAME / "storage.sqlite",
    ]
    missing = [path for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError(
            "Vector Store seed ناقص است: " + ", ".join(str(path) for path in missing)
        )


def prepare_vectorstore(bundle: Path, data_root: Path) -> Path:
    override = os.getenv("RAG_FINANCE_VECTORSTORE_PATH")
    if override:
        vectorstore_root = Path(override).resolve()
        qdrant_path = vectorstore_root / "qdrant_local"
        if not qdrant_path.exists():
            raise FileNotFoundError(f"Vector store not found: {qdrant_path}")
        return vectorstore_root

    seed = bundle / "resources" / "qdrant_local"
    validate_vectorstore_seed(seed)

    target_root = data_root / "vectorstore"
    target = target_root / "qdrant_local"

    if not target.exists():
        target_root.mkdir(parents=True, exist_ok=True)
        shutil.copytree(seed, target)

    return target_root


def preflight_vectorstore(vectorstore_root: Path) -> None:
    """Open the writable local Qdrant copy once, verify the collection, then release it."""
    from qdrant_client import QdrantClient

    qdrant_path = vectorstore_root / "qdrant_local"
    client = QdrantClient(path=str(qdrant_path))
    try:
        collections = client.get_collections().collections
        names = {item.name for item in collections}
        if COLLECTION_NAME not in names:
            raise RuntimeError(
                f"Qdrant collection not found in bundled seed: {COLLECTION_NAME}"
            )
    finally:
        client.close()


def find_port(preferred: int) -> int:
    for port in range(preferred, preferred + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free localhost port found.")


def open_browser_when_ready(port: int) -> None:
    url = f"http://127.0.0.1:{port}"
    deadline = time.time() + 60
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                if 200 <= response.status < 500:
                    webbrowser.open(url)
                    return
        except Exception:
            time.sleep(0.4)


def write_startup_error(error: Exception) -> None:
    path_value = os.getenv("RAG_FINANCE_STARTUP_ERROR_FILE")
    if not path_value:
        return
    try:
        path = Path(path_value)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(str(error), encoding="utf-8")
    except Exception:
        pass


def write_startup_trace(message: str) -> None:
    path_value = os.getenv("RAG_FINANCE_STARTUP_TRACE_FILE")
    if not path_value:
        return
    try:
        path = Path(path_value)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as trace:
            trace.write(message + "\n")
    except Exception:
        pass


def main() -> int:
    try:
        stack_file = None
        stack_path = os.getenv("RAG_FINANCE_STARTUP_STACK_FILE")
        if stack_path:
            stack_file = Path(stack_path).open("w", encoding="utf-8")
            faulthandler.dump_traceback_later(30, repeat=True, file=stack_file)

        bundle = resource_root()
        exe_root = executable_root()
        data_root = writable_root()
        write_startup_trace("runtime roots ready")

        load_runtime_config(exe_root, data_root)
        validate_api_config()
        write_startup_trace("configuration ready")

        vectorstore_root = prepare_vectorstore(bundle, data_root)
        write_startup_trace("vector store copied")
        preflight_vectorstore(vectorstore_root)
        write_startup_trace("vector store preflight passed")
        runtime_app = prepare_runtime_files(bundle, data_root)
        write_startup_trace("runtime files ready")

        os.environ["RAG_FINANCE_RESOURCE_ROOT"] = str(bundle)
        os.environ["RAG_FINANCE_WRITABLE_ROOT"] = str(data_root)
        os.environ["RAG_FINANCE_VECTORSTORE_PATH"] = str(vectorstore_root)

        preferred = int(os.getenv("RAG_FINANCE_PORT", str(DEFAULT_PORT)))
        port = find_port(preferred)
        write_startup_trace(f"selected port: {port}")

        if os.getenv("RAG_FINANCE_DISABLE_BROWSER") != "1":
            threading.Thread(
                target=open_browser_when_ready,
                args=(port,),
                daemon=True,
            ).start()

        from streamlit.web import bootstrap

        write_startup_trace("starting Streamlit")
        bootstrap.run(
            str(runtime_app),
            False,
            [],
            {
                "server.address": "127.0.0.1",
                "server.port": port,
                "server.headless": True,
                "browser.gatherUsageStats": False,
            },
        )
        return 0

    except Exception as exc:
        write_startup_error(exc)
        show_error("RAG Finance", str(exc))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
