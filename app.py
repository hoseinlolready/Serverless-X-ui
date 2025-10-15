import os, threading, time
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

PORT = int(os.getenv("PORT", "8000"))

class IndexHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        message = "<html><body><h1>Server is running</h1></body></html>"
        self.send_header("Content-Length", str(len(message)))
        self.end_headers()
        self.wfile.write(message.encode())
    def log_message(self, *args):  # silence default logging
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def background_job():
    while True:
        print("Background task heartbeat")
        time.sleep(30)

if __name__ == "__main__":
    threading.Thread(target=background_job, daemon=True).start()
    print(f"HTTP server on port {PORT}")
    ThreadedHTTPServer(("0.0.0.0", PORT), IndexHandler).serve_forever()
