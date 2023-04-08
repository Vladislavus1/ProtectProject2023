import sqlite3



connection = sqlite3.connect("../app.db")
# print("DB success")
#
# connection.execute("CREATE TABLE users (name TEXT, password TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)")

password = "admin"
connection.execute(f"INSERT INTO users (name, password) VALUES ('admin', '{password}')")
connection.commit()

print("table successfully added")

connection.close()