from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola, mundo!"

@app.route("/info")
def info():
    return jsonify({"mensaje": "Esta es una aplicación Flask básica"})

if __name__ == "__main__":
    app.run(port=5003)
