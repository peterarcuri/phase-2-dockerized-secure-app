
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "project": "phase-2-dockerized-secure-app",
        "status": "running",
        "security_focus": [
            "minimal Docker image",
            "non-root container user",
            "vulnerability scanning",
            "CI/CD security checks"
        ]
    })


@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




