import sqlite3   #importing

conn = sqlite3.connect("application.db")   #connection python and sql

cursor = conn.cursor()   #creating cursor

#creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS APPLICATIONS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    status TEXT NOT NULL,
    date_applied TEXT
)
""")

#SAVING DATA PARMANENTLY
conn.commit()

#closing 
conn.close()

print("database and table created successfully")