from flask import Flask, render_template, request

app = Flask(__name__)
applications = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        company = request.form.get("company")
        position = request.form.get("position")
        status = request.form.get("status")
        date_applied = request.form.get("date_applied")
        job_link = request.form.get("job_link")
        applications.append({"company": company, "position": position, "status": status, "date_applied": date_applied, "job_link": job_link})

    return render_template("index.html", applications=applications)