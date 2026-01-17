from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("students.db")

# create table
db = get_db()
db.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_no TEXT,
    department TEXT,
    year INTEGER
)
""")
db.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add_student():
    db = get_db()
    db.execute(
        "INSERT INTO students (name, roll_no, department, year) VALUES (?, ?, ?, ?)",
        ("Dolly", "BM01", "Biomedical", 3)
    )
    db.commit()
    db.close()
    return "Student Added"

@app.route("/view")
def view_students():
    db = get_db()
    data = db.execute("SELECT * FROM students").fetchall()
    db.close()
    return str(data)

@app.route("/update")
def update_student():
    db = get_db()
    db.execute(
        "UPDATE students SET year=? WHERE roll_no=?",
        (4, "BM01")
    )
    db.commit()
    db.close()
    return "Student Updated"


@app.route("/delete")
def delete_student():
    db = get_db()
    db.execute(
        "DELETE FROM students WHERE roll_no=?",
        ("BM01",)
    )
    db.commit()
    db.close()
    return "Student Deleted"

app.run()