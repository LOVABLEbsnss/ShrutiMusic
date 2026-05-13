import os
import subprocess
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

    def log_message(self, format, *args):
        pass  # Suppress logs

def start_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("", port), Handler)
    print(f"Health server running on port {port}")
    server.serve_forever()

def start_bot():
    subprocess.run(["python3", "-m", "ShrutiMusic"])

# Start bot in background
bot_thread = threading.Thread(target=start_bot)
bot_thread.daemon = True
bot_thread.start()

# Give bot time to start
time.sleep(3)

# Start health server (blocks main thread)
start_server()
