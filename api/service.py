import sqlite3
from helpers import toDict

def getAll():
    connection = sqlite3.connect("./data/taco.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    data = cursor.execute(
        """
        SELECT description, carbohydrate, protein, fat FROM "taco_table"
        """
    ).fetchall()
    data = toDict(data)
    connection.close()
    return data

def getPattern(pattern):
    connection = sqlite3.connect("./data/taco.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    data = cursor.execute(
        """
        SELECT description FROM "taco_table"
        WHERE description LIKE ?
        LIMIT 10
        """,
        ('%' + pattern + '%',)
    ).fetchall()
    data = toDict(data)
    connection.close()
    return data

def getByID(id):
    connection = sqlite3.connect("./data/taco.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    data = cursor.execute(
        """
        SELECT * FROM "taco_table"
        WHERE id = ?
        """,
        (id,)
    ).fetchall()
    data = toDict(data)
    connection.close()
    return data

