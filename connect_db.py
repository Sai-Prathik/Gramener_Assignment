import sqlite3

conn = sqlite3.connect('database.db')
conn.execute("CREATE TABLE contents(id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
conn.close()