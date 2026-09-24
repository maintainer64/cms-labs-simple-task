#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import socket
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def command(*arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(arguments, check=False, capture_output=True, text=True, timeout=3)


def service_running(name: str) -> bool:
    for process_name in Path("/proc").glob("[0-9]*/comm"):
        try:
            if process_name.read_text(encoding="utf-8").strip() == name:
                return True
        except (FileNotFoundError, PermissionError):
            continue
    return False


def ssh_ready() -> bool:
    try:
        with socket.create_connection(("127.0.0.1", 22), timeout=1):
            return True
    except OSError:
        return False


def state() -> dict[str, object]:
    interfaces: dict[str, dict[str, object]] = {}
    result = command("ip", "-j", "address", "show")
    if result.returncode == 0:
        for interface in json.loads(result.stdout):
            interfaces[interface["ifname"]] = {
                "state": interface.get("operstate", "UNKNOWN"),
                "addresses": [
                    f"{address['local']}/{address['prefixlen']}"
                    for address in interface.get("addr_info", [])
                    if address.get("family") == "inet"
                ],
            }

    peer = os.environ.get("LAB_PEER", "")
    ping = command("ping", "-c", "1", "-W", "1", peer) if peer else None
    return {
        "hostname": socket.gethostname(),
        "interfaces": interfaces,
        "peer": peer,
        "peer_reachable": ping is not None and ping.returncode == 0,
        "services": {"ssh": ssh_ready(), "snmp": service_running("snmpd")},
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - method name is defined by BaseHTTPRequestHandler
        if self.path == "/healthz":
            payload = {"status": "ok"}
        elif self.path == "/state":
            payload = state()
        else:
            self.send_error(404)
            return
        encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format: str, *arguments: object) -> None:
        return


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
