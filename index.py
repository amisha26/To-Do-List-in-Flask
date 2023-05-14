from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    conn = db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks = tasks)


# @app.route("/add", methods = ['POST'])
# def add_task():


if __name__ == 'main':
    app.run(port = 5000, debug = True)