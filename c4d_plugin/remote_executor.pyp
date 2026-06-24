import socket
import socketserver
import threading
import traceback

import c4d


HOST = "127.0.0.1"
PORT = 4567

_server = None
_server_thread = None
_globals = {
    "__name__": "__c4d_remote_executor__",
    "c4d": c4d,
}


class RemoteExecutorHandler(socketserver.BaseRequestHandler):
    def handle(self):
        peer_host = self.client_address[0]
        if peer_host not in ("127.0.0.1", "::1"):
            self.request.sendall(b"ERROR: remote connections are not allowed\n")
            return

        chunks = []
        while True:
            chunk = self.request.recv(65536)
            if not chunk:
                break
            chunks.append(chunk)

        code = b"".join(chunks).decode("utf-8")
        result = execute_code(code)
        self.request.sendall(result.encode("utf-8", "replace"))


class LocalThreadingTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True
    address_family = socket.AF_INET


def execute_code(code):
    try:
        c4d.EventAdd()
        exec(code, _globals)
        c4d.EventAdd()
        return "OK\n"
    except Exception:
        c4d.EventAdd()
        return "ERROR\n" + traceback.format_exc()


def start_server():
    global _server, _server_thread

    if _server is not None:
        return

    try:
        _server = LocalThreadingTCPServer((HOST, PORT), RemoteExecutorHandler)
    except OSError:
        _server = None
        raise

    _server_thread = threading.Thread(
        target=_server.serve_forever,
        name="C4DRemoteExecutor",
    )
    _server_thread.daemon = True
    _server_thread.start()
    print("C4D Remote Executor listening on %s:%d" % (HOST, PORT))


def stop_server():
    global _server, _server_thread

    if _server is None:
        return

    _server.shutdown()
    _server.server_close()
    _server = None
    _server_thread = None


def PluginMessage(message_id, data):
    if message_id == getattr(c4d, "C4DPL_PROGRAM_STARTED", None):
        try:
            start_server()
        except Exception:
            print("C4D Remote Executor failed to start:")
            print(traceback.format_exc())
    elif message_id == getattr(c4d, "C4DPL_ENDACTIVITY", None):
        stop_server()

    return True


if __name__ == "__main__":
    try:
        start_server()
    except Exception:
        print("C4D Remote Executor failed to start:")
        print(traceback.format_exc())
