import sqlite3

conn = sqlite3.connect("volunteer.db")
print("database opened successfully ")
conn.execute(
    """create table Donor(first_name TEXT NOT NULL, last_name TEXT 
    NOT NULL, phone_No LONG NOT NULL, email TEXT NOT NULL,blood_group TEXT NOT NULL,dob DATE NOT NULL,
    loc TEXT NOT NULL)"""
)
print("Table created successfully")
conn.close()
