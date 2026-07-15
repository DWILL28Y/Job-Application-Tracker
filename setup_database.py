import sqlite3

connection = sqlite3.connect("applications.db")
cursor = connection.cursor()



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

connection.commit()
connection.close()
