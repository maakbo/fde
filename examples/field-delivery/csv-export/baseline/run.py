#!/usr/bin/env python3
"""Build the synthetic Java case in a temporary directory and test or serve locally."""
import argparse
from pathlib import Path
from queue import Queue, Empty
import subprocess
import sys
import tempfile
from threading import Thread
sys.dont_write_bytecode = True
from acceptance import verify

parser = argparse.ArgumentParser()
parser.add_argument("--serve", action="store_true", help="open a localhost demo until Ctrl-C")
args = parser.parse_args()
root = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix="fde-order-search-") as build:
    subprocess.run(["javac", "--release", "16", "-d", build,
                    *map(str, sorted(root.glob("*.java")))], check=True)
    subprocess.run(["java", "-cp", build, "OrderSearchTest"], check=True)
    server = subprocess.Popen(["java", "-cp", build, "OrderSearchServer", "0"],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    lines = Queue()
    def collect():
        for line in server.stdout:
            lines.put(line.strip())
    Thread(target=collect, daemon=True).start()
    try:
        while True:
            try:
                line = lines.get(timeout=10)
            except Empty:
                raise RuntimeError("Local server did not announce its port")
            if line.startswith("PORT="):
                port = int(line.split("=", 1)[1])
                break
            print(line)
        base = f"http://127.0.0.1:{port}"
        verify(base)
        if args.serve:
            print(f"Demo: {base}/ (Ctrl-C to stop)", flush=True)
            try:
                server.wait()
            except KeyboardInterrupt:
                pass
    finally:
        server.terminate()
        try:
            server.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server.kill()
            server.wait()
