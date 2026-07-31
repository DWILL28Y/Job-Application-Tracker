Job Application Tracker

A simple web application for organizing and tracking job applications in one place.

The project is built with Python, Flask, SQLite, HTML, Jinja, and Bootstrap. It allows users to save job application details, view current applications, track application statuses, and remove records they no longer need.

Features
- Add a new job application
- Record the company and position
- Select an application status
- Save the date applied
- Save an optional link to the job posting
- Display all saved applications
- Show the total number of applications in each status
- Delete individual applications
- Store application data locally with SQLite
- Responsive styling using Bootstrap
- Application Statuses

Applications can be organized into the following categories:

- Interested
- Applied
- Interviewing
- Offered
- Rejected

Technologies Used
- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja
- Bootstrap
- Git and GitHub


Database

The application uses SQLite to store job application records.

The local database file is excluded from GitHub through .gitignore. Each person who downloads the project should run setup_database.py to create their own database.

The database stores:

- Application ID
- Company
- Position
- Status
- Date applied
- Job posting link
  
What I Learned

This project gave me experience with:
- Creating routes with Flask
- Handling GET and POST requests
- Retrieving submitted HTML form data
- Using parameterized SQL queries
- Creating, reading, and deleting SQLite records
- Passing Python data into Jinja templates
- Using loops and conditional statements in HTML templates
- Organizing Flask templates and static files
- Styling an application with Bootstrap


Project Status

This project is currently under development as part of my software-development portfolio. 
Additional features and design improvements will be added over time.
