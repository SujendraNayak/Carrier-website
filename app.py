from flask import Flask, render_template, jsonify
from database import load_jobs_from_db 
#from database import load_job_from_db# import from database.py

app = Flask(__name__)

@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template('home.html', JOBS=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_jobs_from_db()
    #return jsonify(job)
   # job = next((job for job in job if job["id"] == id), None)
    if not job:
        return "Job not found", 404
    return render_template("jobpage.html", job=job)


if __name__ == '__main__':
    app.run(debug=True)
