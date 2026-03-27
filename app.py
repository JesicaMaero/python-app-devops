from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    db = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="testdb"
    )

    cursor = db.cursor()
    cursor.execute("SELECT id, description FROM items")

    rows = cursor.fetchall()

    html = "<h1>Hola UTN - Práctica DevOps</h1>"

    for row in rows:
        html += f"<p>Registro ID = {row[0]} - {row[1]}</p>"

    return html

app.run(host="0.0.0.0", port=80)
