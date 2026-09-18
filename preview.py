#!/usr/bin/env python3
"""
로컬 프리뷰 서버 (표준 라이브러리만 사용).

    python3 preview.py
    → http://127.0.0.1:4174/

HTML/CSS/JS 파일이 바뀌면 브라우저가 자동으로 새로고침된다.
(현재 폴더의 파일 mtime을 폴링하는 방식 — 별도 설치 불필요)
"""
import http.server
import os
import socketserver
import threading
import time

HOST = "127.0.0.1"
PORT = 4174
WATCH_EXT = (".html", ".css", ".js")

# 감시할 파일들의 최신 변경 시각(state)
_state = {"stamp": 0.0}

# 페이지에 주입할 자동 새로고침 스크립트
_RELOAD_JS = """
<script>
(function () {
  let last = null;
  setInterval(function () {
    fetch("/__reload", { cache: "no-store" })
      .then(function (r) { return r.text(); })
      .then(function (s) {
        if (last === null) { last = s; return; }
        if (s !== last) { location.reload(); }
      })
      .catch(function () {});
  }, 1000);
})();
</script>
"""


def _scan_stamp():
    latest = 0.0
    for root, _dirs, files in os.walk("."):
        if "/.git" in root or root.startswith("./.git"):
            continue
        for f in files:
            if f.endswith(WATCH_EXT):
                try:
                    latest = max(latest, os.path.getmtime(os.path.join(root, f)))
                except OSError:
                    pass
    return latest


def _watch():
    while True:
        _state["stamp"] = _scan_stamp()
        time.sleep(0.7)


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):  # 조용하게
        pass

    def do_GET(self):
        if self.path == "/__reload":
            body = str(_state["stamp"]).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            return
        return super().do_GET()

    def send_head(self):
        # .html 응답에 자동 새로고침 스크립트 주입
        path = self.translate_path(self.path)
        if path.endswith(".html") and os.path.isfile(path):
            with open(path, "rb") as fp:
                data = fp.read()
            inject = _RELOAD_JS.encode()
            if b"</body>" in data:
                data = data.replace(b"</body>", inject + b"</body>", 1)
            else:
                data += inject
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self._injected = data
            from io import BytesIO
            return BytesIO(data)
        return super().send_head()


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)) or ".")
    _state["stamp"] = _scan_stamp()
    threading.Thread(target=_watch, daemon=True).start()

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
        print(f"▶ 프리뷰 실행 중 : http://{HOST}:{PORT}/")
        print("  파일 저장 시 자동 새로고침 · 종료: Ctrl+C")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n■ 종료")


if __name__ == "__main__":
    main()
