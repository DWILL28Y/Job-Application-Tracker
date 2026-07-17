

import sqlite3

#Used this file to check if the database was working
connection = sqlite3.connect("applications.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM applications")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()