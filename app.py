from Flask import Flask, jsonify

app = Flask(__name__)

TASK = [
    {"id": 1, "title": "Estudar Docker"},
    {"id": 2, "title": "Criar Docker"}    
]

@app.get("/")
def index():
    return jsonify(TASK)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)