#!/usr/bin/env python3
"""Reproduce the fictional CSV delivery locally; requires Python 3.9+ and JDK 16+."""
import argparse
from contextlib import contextmanager
import json
from pathlib import Path
from queue import Queue, Empty
import socket
import subprocess
import sys
import tempfile
from threading import Thread
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parent

def run(*args, **kwargs):
    return subprocess.run(list(map(str, args)), check=True, timeout=120, **kwargs)

@contextmanager
def server(build):
    process = subprocess.Popen(['java', '-cp', str(build), 'OrderSearchServer', '0'],
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    lines = Queue()
    def collect():
        for line in process.stdout:
            lines.put(line.strip())
    Thread(target=collect, daemon=True).start()
    port = None
    try:
        for _ in range(20):
            try:
                line = lines.get(timeout=10)
            except Empty:
                raise RuntimeError('Server startup timed out')
            if line.startswith('PORT='):
                port = int(line.split('=', 1)[1])
                break
        if port is None:
            raise RuntimeError('Server did not announce a port')
        yield 'http://127.0.0.1:' + str(port)
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)
        process.stdout.close()
        if port is not None:
            with socket.socket() as probe:
                probe.settimeout(1)
                if probe.connect_ex(('127.0.0.1', port)) == 0:
                    raise RuntimeError('Port remained open after stop')
            print('PASS stopped server; port closed')

def fetch(base, path):
    try:
        with urllib.request.urlopen(base + path, timeout=5) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as error:
        return error.code, error.read()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--browser', action='store_true', help='also use Node, Playwright and an installed browser')
    args = parser.parse_args()
    run(sys.executable, ROOT / 'implementation/run.py')
    with tempfile.TemporaryDirectory(prefix='fde-csv-replay-') as temporary:
        build = Path(temporary) / 'current'
        build.mkdir()
        run('javac', '--release', '16', '-d', build,
            *sorted((ROOT / 'implementation').glob('*.java')),
            ROOT / 'acceptance/SpecialCsvHarness.java', ROOT / 'forward/AlternateCsvHarness.java')
        special = Path(temporary) / 'special.csv'
        alternate = Path(temporary) / 'alternate.csv'
        for harness, output in [('SpecialCsvHarness', special), ('AlternateCsvHarness', alternate)]:
            with output.open('wb') as stream:
                run('java', '-cp', build, harness, stdout=stream)
        run(sys.executable, ROOT / 'forward/verify_alternate.py', alternate)
        query = '/orders?status=NEW&from=2026-10-02&to=2026-10-04'
        with server(build) as base:
            for flags in [[], ['-O']]:
                run(sys.executable, *flags, ROOT / 'acceptance/acceptance.py', '--base-url', base,
                    '--csv-path', '/orders.csv', '--special-csv-file', special)
            status, body = fetch(base, query)
            current = json.loads(body)
            if status != 200:
                raise RuntimeError('Current search failed')
            if args.browser:
                run('node', ROOT / 'browser/browser-check.cjs', base)
        old = Path(temporary) / 'baseline'
        old.mkdir()
        run('javac', '--release', '16', '-d', old, *sorted((ROOT / 'baseline').glob('*.java')))
        run('java', '-cp', old, 'OrderSearchTest')
        with server(old) as base:
            status, body = fetch(base, query)
            if status != 200 or json.loads(body) != current:
                raise RuntimeError('Baseline search differs')
            if fetch(base, '/orders.csv')[0] != 404:
                raise RuntimeError('Baseline unexpectedly has CSV')
            print('PASS baseline restart: same search; CSV unavailable')
    print('PASS local replay; actual team adoption and business effects remain unmeasured')

if __name__ == '__main__':
    main()
