from __future__ import annotations

import os
import json
import logging
import shutil
import socket
import sys
import threading
import time
import urllib.request
import webbrowser
from pathlib import Path
from datetime import datetime, timezone

from dotenv import load_dotenv


APP_NAME = "RAGFinance"
DEFAULT_PORT = 8501
COLLECTION_NAME = "financial_knowledge_base"
HEALTH_PATH = "/_stcore/health"
STARTUP_TIMEOUT_SECONDS = 90


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


def find_port(preferred: int = DEFAULT_PORT) -> int:
    for port in range(preferred, preferred + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free localhost port found.")


def _read_url(url: str) -> tuple[int, str]:
    with urllib.request.urlopen(url, timeout=2) as response:
        return response.status, response.read(8192).decode("utf-8", errors="replace")


def wait_for_application(port: int, timeout: int = STARTUP_TIMEOUT_SECONDS) -> str:
    url = f"http://127.0.0.1:{port}/"
    health_url = f"http://127.0.0.1:{port}{HEALTH_PATH}"
    deadline = time.time() + timeout
    last_error = "server did not answer"
    while time.time() < deadline:
        try:
            health_status, health_body = _read_url(health_url)
            root_status, root_body = _read_url(url)
            if (
                health_status == 200
                and health_body.strip().lower() == "ok"
                and root_status == 200
                and "streamlit" in root_body.lower()
                and "not found" not in root_body.lower()
            ):
                return url
            last_error = (
                f"health={health_status}, root={root_status}, "
                f"health_body={health_body[:40]!r}"
            )
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"
        time.sleep(0.4)
    raise TimeoutError(f"Application was not ready on {url}: {last_error}")


def write_launch_state(data_root: Path, port: int, status: str) -> None:
    state = {
        "pid": os.getpid(),
        "selected_port": port,
        "root_url": f"http://127.0.0.1:{port}/",
        "health_url": f"http://127.0.0.1:{port}{HEALTH_PATH}",
        "status": status,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    path = data_root / "runtime" / "launch-state.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2), encoding="utf-8")


def ready_actions(port: int, data_root: Path) -> None:
    try:
        configure_logging(data_root)
        url = wait_for_application(port)
        write_launch_state(data_root, port, "ready")
        (data_root / "runtime" / "browser-url.txt").write_text(url, encoding="utf-8")
        logging.info("Application ready: %s", url)

        e2e_result = os.getenv("RAG_FINANCE_E2E_RESULT_FILE")
        if e2e_result:
            from src.runtime_e2e import run_runtime_e2e

            run_runtime_e2e(Path(e2e_result), data_root)

        if os.getenv("RAG_FINANCE_DISABLE_BROWSER") != "1":
            webbrowser.open(url)
            logging.info("Default browser requested for %s", url)
    except Exception as exc:
        logging.exception("Application readiness failed")
        write_startup_error(exc)
        show_error(
            "RAG Finance",
            "RAG Finance could not start. Please restart the application.",
        )


def install_server_ready_hook(bootstrap, port: int, data_root: Path) -> None:
    original_on_server_start = bootstrap._on_server_start

    def on_server_start(server) -> None:
        original_on_server_start(server)
        threading.Thread(
            target=ready_actions,
            args=(port, data_root),
            daemon=True,
        ).start()

    bootstrap._on_server_start = on_server_start


def configure_logging(data_root: Path) -> None:
    log_dir = data_root / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        filename=log_dir / "launcher.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )


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
        bundle = resource_root()
        exe_root = executable_root()
        data_root = writable_root()
        write_launch_state(data_root, 0, "initializing")
        write_startup_trace("runtime roots ready")

        load_runtime_config(exe_root, data_root)
        validate_api_config()
        write_startup_trace("configuration ready")

        write_launch_state(data_root, 0, "preparing-vectorstore")
        vectorstore_root = prepare_vectorstore(bundle, data_root)
        write_startup_trace("vector store copied")
        preflight_vectorstore(vectorstore_root)
        write_startup_trace("vector store preflight passed")
        write_launch_state(data_root, 0, "preparing-runtime")
        runtime_app = prepare_runtime_files(bundle, data_root)
        write_startup_trace("runtime files ready")

        os.environ["RAG_FINANCE_RESOURCE_ROOT"] = str(bundle)
        os.environ["RAG_FINANCE_WRITABLE_ROOT"] = str(data_root)
        os.environ["RAG_FINANCE_VECTORSTORE_PATH"] = str(vectorstore_root)

        # Production always starts from the application-owned preference. An
        # unrelated user/machine environment variable must not redirect the UI.
        port = find_port(DEFAULT_PORT)
        write_startup_trace(f"selected port: {port}")
        write_launch_state(data_root, port, "starting")
        logging.info("Selected loopback port %s", port)
        os.environ["STREAMLIT_SERVER_ADDRESS"] = "127.0.0.1"
        os.environ["STREAMLIT_SERVER_PORT"] = str(port)
        os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
        os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"
        os.environ["STREAMLIT_SERVER_RUN_ON_SAVE"] = "false"
        os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"
        os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"

        write_launch_state(data_root, port, "loading-streamlit")
        from streamlit import config as streamlit_config
        from streamlit.web import bootstrap

        flag_options = {
            "global.developmentMode": False,
            "server.address": "127.0.0.1",
            "server.port": port,
            "server.headless": True,
            "server.fileWatcherType": "none",
            "server.runOnSave": False,
            "browser.gatherUsageStats": False,
        }
        streamlit_config._main_script_path = str(runtime_app)
        bootstrap.load_config_options(flag_options=flag_options)
        # A frozen desktop client never hot-reloads config or source files.
        # Avoid starting Streamlit's polling watchers before the server binds.
        bootstrap._install_config_watchers = lambda _flag_options: None
        install_server_ready_hook(bootstrap, port, data_root)
        write_startup_trace("starting Streamlit")
        write_launch_state(data_root, port, "starting-streamlit")
        bootstrap.run(
            str(runtime_app),
            False,
            [],
            flag_options,
        )
        return 0

    except Exception as exc:
        logging.exception("Launcher failed")
        write_startup_error(exc)
        show_error(
            "RAG Finance",
            "RAG Finance could not start. Please restart the application.",
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
