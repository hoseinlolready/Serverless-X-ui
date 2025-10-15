from flask import Flask
import os
import threading

app = Flask(__name__)

# Your continuous command (example: run a bot, tunnel, etc.)
CMD = "curl -sSf https://sshx.io/get | sh -s run"  # replace this with your command

def run_cmd():
    os.system(CMD)

@app.route('/')
def home():
    return '✅ Server and background command running!'

if __name__ == '__main__':
    # Start command in background thread so Flask can still run
    threading.Thread(target=run_cmd, daemon=True).start()

    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
