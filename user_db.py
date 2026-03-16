import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     firstname TEXT NOT NULL,
     lastname TEXT NOT NULL,
     email TEXT NOT NULL,
     phone TEXT NOT NULL,
     password TEXT NOT NULL
     )
""")
print("users table successfully created")
conn.commit()
conn.close()