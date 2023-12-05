import sqlite3
from helpers import toDict
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    connection = sqlite3.connect("./data/taco.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    data = cursor.execute("""
        SELECT * FROM "taco_table"
    """).fetchall()
    data = toDict(data)
    return jsonify(data)
