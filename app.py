from flask import Flask, jsonify

app = Flask(__name__)

TASKS = [
{"id": 1, "title": "Estudar Docker"},
{"id": 2, "title": "Criar o pipeline"},
]

@app.get("/")
def index():
    return jsonify(status="online")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/tasks")
def tasks():
    return jsonify(TASKS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)