import os

from flask import Flask, jsonify

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "local")
<<<<<<< HEAD
APP_VERSION = os.getenv("APP_VERSION", "0.3.0")
=======
APP_VERSION = os.getenv("APP_VERSION", "0.2.0")
>>>>>>> origin/main


@app.route("/")
def index():
    return jsonify(message="Hello from demo-app", env=APP_ENV, version=APP_VERSION)


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
