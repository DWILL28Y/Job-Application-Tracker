import sqlite3

connection = sqlite3.connect("applications.db")
conn = sqlite3.connect("applications.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    position TEXT NOT NULL,
    status TEXT NOT NULL,
    date_applied DATE,
    job_link TEXT
)
''')

conn.commit()
conn.close()
connection.close()
