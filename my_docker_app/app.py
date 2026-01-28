from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "docker-demo-app"
    })

@app.route("/")
def index():
    return "Docker container is running successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

