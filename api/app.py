import service
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    if request.args.get("pattern"):
        pattern = request.args.get("pattern")
        data = service.getPattern(pattern)
        return data
    data = service.getAll()
    return jsonify(data)

@app.route("/food/<id>")
def getByID(id):
    data = service.getByID(id)
    return jsonify(data)
