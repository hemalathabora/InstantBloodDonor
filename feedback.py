import sqlite3
from flask import  Flask
app = Flask(__name__)
conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback(
id INTEGER PRIMARY KEY,
content TEXT,
rating INTEGER)
''')
conn.commit()
conn.close()