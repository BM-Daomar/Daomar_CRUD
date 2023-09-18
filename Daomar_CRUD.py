import sqlite3

# Create or connect to the database file
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

# Create a table for your CRUD operation
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT
                )''')

conn.commit()
conn.close()
