import http.server
import importlib.util
import socket
import sys
import threading
import types
import unittest
from pathlib import Path

if "dotenv" not in sys.modules:
    dotenv_stub = types.ModuleType("dotenv")
    dotenv_stub.load_dotenv = lambda *_args, **_kwargs: None
    sys.modules["dotenv"] = dotenv_stub

_launcher_path = Path(__file__).resolve().parents[1] / "packaging" / "windows" / "launcher.py"
_spec = importlib.util.spec_from_file_location("rag_finance_launcher", _launcher_path)
launcher = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(launcher)


class _StreamlitHandler(http.server.BaseHTTPRequestHandler):
    root_body = b"<html><body>Streamlit</body></html>"

    def do_GET(self):
        if self.path == launcher.HEALTH_PATH:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")
        elif self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(self.root_body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *_args):
        pass


class WindowsLauncherTests(unittest.TestCase):
    def test_port_collision_selects_another_port(self):
        with socket.socket() as occupied:
            occupied.bind(("127.0.0.1", 0))
            preferred = occupied.getsockname()[1]
            self.assertNotEqual(launcher.find_port(preferred), preferred)

    def test_ready_requires_streamlit_root(self):
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _StreamlitHandler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            port = server.server_address[1]
            self.assertEqual(
                launcher.wait_for_application(port, timeout=2),
                f"http://127.0.0.1:{port}/",
            )
        finally:
            server.shutdown()
            server.server_close()

    def test_not_found_root_is_rejected(self):
        original = _StreamlitHandler.root_body
        _StreamlitHandler.root_body = b"Not Found"
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), _StreamlitHandler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            with self.assertRaises(TimeoutError):
                launcher.wait_for_application(server.server_address[1], timeout=1)
        finally:
            _StreamlitHandler.root_body = original
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main()
