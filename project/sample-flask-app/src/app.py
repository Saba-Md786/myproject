from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker!"

if __name__ == '__main__':
    # Important: 0.0.0.0 makes it accessible from Docker container
    app.run(host="0.0.0.0", port=80)

