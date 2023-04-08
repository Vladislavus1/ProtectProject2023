import random
import sqlite3
from flask_login import UserMixin, AnonymousUserMixin


connection = sqlite3.connect("../app.db", check_same_thread=False)
cursor = connection.cursor()

class User(UserMixin, AnonymousUserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

def func(selector, value):
    cursor.execute(f"SELECT * FROM users WHERE {selector} = '{value}' ")
    user_data = cursor.fetchall()

    if len(user_data) == 0:
        return None
    user_data = user_data[0]
    user = User(user_data[2], user_data[0], user_data[1])
    return user