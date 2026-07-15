from dbm import sqlite3
from multiprocessing.dummy import connection
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
applications = []

@app.route("/", methods=["GET", "POST"])
def home():
    connection = sqlite3.connect("applications.db")
    cursor = connection.cursor()
    if request.method == "POST":
        company = request.form.get("company")
        position = request.form.get("position")
        status = request.form.get("status")
        date_applied = request.form.get("date_applied")
        job_link = request.form.get("job_link")
        #applications.append({"company": company, "position": position, "status": status, "date_applied": date_applied, "job_link": job_link})
        
        
        app_query = "INSERT INTO applications (company, position, status, date_applied, job_link) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(app_query, (company, position, status, date_applied, job_link))

    cursor.execute("SELECT * FROM applications")

    rows = cursor.fetchall()
    for row in rows:
        print(row)


    connection.commit()
    connection.close()

    return render_template("index.html", applications=rows)