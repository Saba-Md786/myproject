from flask import Flask, render_template_string
import mysql.connector
import redis
import time
import sys

app = Flask(__name__)

# -----------------------------
# MySQL connection with retry
# -----------------------------
def get_mysql_connection(retries=10, delay=5):
    for attempt in range(retries):
        try:
            conn = mysql.connector.connect(
                host="mysql",
                user="root",
                password="root123",
                database="shop"
            )
            print("✅ MySQL connected")
            return conn
        except mysql.connector.Error:
            print(f"⏳ Waiting for MySQL... ({attempt + 1}/{retries})")
            time.sleep(delay)

    sys.exit("❌ MySQL connection failed")

db = get_mysql_connection()

# -----------------------------
# Redis connection
# -----------------------------
r = redis.Redis(host="redis", port=6379, decode_responses=True)

# -----------------------------
# UI Template
# -----------------------------
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Docker Compose Dashboard</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
      color: #fff;
    }
    .container {
      max-width: 900px;
      margin: 60px auto;
      background: #ffffff10;
      backdrop-filter: blur(10px);
      padding: 40px;
      border-radius: 16px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }
    h1 {
      text-align: center;
      margin-bottom: 10px;
    }
    .subtitle {
      text-align: center;
      opacity: 0.8;
      margin-bottom: 40px;
    }
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
    }
    .card {
      background: #ffffff20;
      padding: 25px;
      border-radius: 12px;
      text-align: center;
      transition: transform 0.3s;
    }
    .card:hover {
      transform: translateY(-5px);
    }
    .card h3 {
      margin-bottom: 10px;
      font-size: 20px;
    }
    .value {
      font-size: 28px;
      font-weight: bold;
      color: #00ffd5;
    }
    footer {
      text-align: center;
      margin-top: 40px;
      font-size: 14px;
      opacity: 0.7;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>🚀 Docker Compose Project</h1>
    <p class="subtitle">Multi-service Python · MySQL · Redis</p>

    <div class="cards">
      <div class="card">
        <h3>Service Status</h3>
        <div class="value">RUNNING</div>
      </div>

      <div class="card">
        <h3>Redis Hits</h3>
        <div class="value">{{ hits }}</div>
      </div>

      <div class="card">
        <h3>MySQL</h3>
        <div class="value">CONNECTED</div>
      </div>
    </div>

    <footer>
      Built with Docker Compose | DevOps Demo Project
    </footer>
  </div>

</body>
</html>
"""

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    hits = r.incr("hits")
    return render_template_string(HTML_TEMPLATE, hits=hits)

# -----------------------------
# App start
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

