from flask import Flask, render_template
import mysql.connector
import time

app = Flask(__name__)

def connect_with_retry():
    retries = 10
    delay = 3

    for i in range(retries):
        try:
            db = mysql.connector.connect(
                host="mysql",
                user="root",
                password="root",
                database="testdb",
                charset="utf8mb4"
            )
            print("✅ Conectado a MySQL")
            return db
        except Exception as e:
            print(f"⏳ Intento {i+1}/{retries} - esperando DB...")
            time.sleep(delay)

    raise Exception("❌ No se pudo conectar a la base de datos")

@app.route("/")
def home():
    db = connect_with_retry()  # 👈 cambio clave
    cursor = db.cursor()

    cursor.execute("SELECT id, description FROM items")
    rows = cursor.fetchall()

    cursor.execute("SELECT name, initials FROM members")
    members = [{"name": r[0], "initials": r[1]} for r in cursor.fetchall()]

    return render_template("index.html", rows=rows, members=members)

app.run(host="0.0.0.0", port=80)