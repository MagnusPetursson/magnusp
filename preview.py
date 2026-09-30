"""Local preview for both languages, with auto-rebuild and live reload.

    python preview.py            # http://localhost:8000  (Icelandic at /is/)
    python preview.py --port 9000

Builds English then Icelandic into site/, serves it, and rebuilds whenever
anything in docs/, docs-is/, overrides/ or the configs changes. Open pages reload
themselves after each rebuild.
"""

import argparse
import functools
import http.server
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
WATCH = [ROOT / "docs", ROOT / "docs-is", ROOT / "overrides", ROOT / "zensical.toml", ROOT / "zensical.is.toml"]
BUILDS = [
    ["zensical", "build", "--clean"],
    ["zensical", "build", "-f", "zensical.is.toml"],
]
RELOAD_JS = b"""<script>
(()=>{let v=null;setInterval(async()=>{try{const r=await fetch('/__build');const n=await r.text();
if(v!==null&&n!==v)location.reload();v=n}catch(e){}},1000)})();
</script></body>"""

build_id = 0
lock = threading.Lock()


def build():
    global build_id
    with lock:
        started = time.time()
        for cmd in BUILDS:
            result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
            output = (result.stdout + result.stderr).strip()
            if result.returncode != 0 or "No issues found" not in output:
                print(output, flush=True)
            if result.returncode != 0:
                print(f"!! build failed: {' '.join(cmd)}", flush=True)
                return
        build_id += 1
        print(f"built in {time.time() - started:.1f}s", flush=True)


def snapshot():
    files = []
    for path in WATCH:
        files.extend([path] if path.is_file() else path.rglob("*"))
    return {f: f.stat().st_mtime for f in files if f.is_file()}


def watch():
    last = snapshot()
    while True:
        time.sleep(0.5)
        current = snapshot()
        if current != last:
            last = current
            build()


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/__build":
            return self.respond(str(build_id).encode(), "text/plain")
        path = Path(self.translate_path(self.path))
        if path.is_dir():
            path = path / "index.html"
        if path.suffix == ".html" and path.is_file():
            html = path.read_bytes().replace(b"</body>", RELOAD_JS, 1)
            return self.respond(html, "text/html; charset=utf-8")
        if not path.exists():
            not_found = SITE / "404.html"
            if not_found.is_file():
                html = not_found.read_bytes().replace(b"</body>", RELOAD_JS, 1)
                return self.respond(html, "text/html; charset=utf-8", 404)
        return super().do_GET()

    def respond(self, body, content_type, status=200):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    port = parser.parse_args().port

    build()
    threading.Thread(target=watch, daemon=True).start()
    handler = functools.partial(Handler, directory=str(SITE))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
    print(f"Preview: http://localhost:{port}/  (Icelandic: http://localhost:{port}/is/)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
