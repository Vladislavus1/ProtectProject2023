import sqlite3
from app import app
from flask import g
from flask import render_template

def add_account(name, password):
    request = f"""INSERT INTO users (name, password) VALUES {name, password}"""
    msg = ""
    try:
        with sqlite3.connect("../app.db") as connection:
            cursor = connection.cursor()
            cursor.execute(request)
            connection.commit()
            msg = "Successfully added"
    except Exception as e:
        connection.rollback()
        msg = str(e)
    finally:
        connection.close()
        return render_template("main.html", msg=msg)

def get_db(name=None):
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("../app.db")
        cursor = db.cursor()
        if name is None:
            all_data = cursor.execute("SELECT name FROM sqlite_schema WHERE type = 'table'").fetchall()
        else:
            cursor.execute(f"select * from {name}")
            all_data = cursor.fetchall()
            all_data = [list(tu) for tu in all_data]
        return all_data

def check_user(username):
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("../app.db")
        cursor = db.cursor()
        cursor.execute(f"select * from users where name = '{username}'")
        all_data = cursor.fetchall()
        all_data = [list(tu) for tu in all_data]
        return all_data