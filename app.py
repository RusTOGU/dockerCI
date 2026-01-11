from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(status="ok", service="flask-web-service")


@app.get("/health")
def health():
    return jsonify(status="healthy")


@app.get("/add")
def add():
    x = request.args.get("x", type=float)
    y = request.args.get("y", type=float)

    if x is None or y is None:
        return jsonify(error="Please provide query params x and y"), 400

    return jsonify(x=x, y=y, result=x + y)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
