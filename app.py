import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    message = os.environ.get("APP_MESSAGE", "no message set")
    return f"Service Models Lab 2 — {message}"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
