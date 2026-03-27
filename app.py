from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    db = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="testdb",
        charset="utf8mb4"
    )
    cursor = db.cursor()

    cursor.execute("SELECT id, description FROM items")
    rows = cursor.fetchall()

    cursor.execute("SELECT name, initials FROM members")
    members = [{"name": r[0], "initials": r[1]} for r in cursor.fetchall()]

    return render_template("index.html", rows=rows, members=members)

app.run(host="0.0.0.0", port=80)
