import argparse
import socket
import sys
from pathlib import Path


HOST = "127.0.0.1"
PORT = 4567


def send_script(path, host=HOST, port=PORT):
    code = path.read_text(encoding="utf-8")

    with socket.create_connection((host, port), timeout=10) as sock:
        sock.settimeout(None)
        sock.sendall(code.encode("utf-8"))
        sock.shutdown(socket.SHUT_WR)

        chunks = []
        while True:
            chunk = sock.recv(65536)
            if not chunk:
                break
            chunks.append(chunk)

    return b"".join(chunks).decode("utf-8", "replace")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Send a Python script to the running Cinema 4D Remote Executor."
    )
    parser.add_argument("script", type=Path, help="Path to a .py script to run in C4D.")
    parser.add_argument("--host", default=HOST, help="Executor host. Defaults to 127.0.0.1.")
    parser.add_argument("--port", type=int, default=PORT, help="Executor port. Defaults to 4567.")
    args = parser.parse_args(argv)

    if args.script.suffix.lower() != ".py":
        parser.error("script must be a .py file")

    if not args.script.is_file():
        parser.error("script does not exist: %s" % args.script)

    try:
        response = send_script(args.script, args.host, args.port)
    except OSError as exc:
        print("ERROR: could not connect to C4D Remote Executor: %s" % exc, file=sys.stderr)
        return 1

    print(response, end="" if response.endswith("\n") else "\n")
    return 0 if response.startswith("OK") else 1


if __name__ == "__main__":
    raise SystemExit(main())
