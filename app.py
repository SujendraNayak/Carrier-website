from flask import Flask, render_template, jsonify
from database import load_jobs_from_db  # import from database.py

app = Flask(__name__)

@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template('home.html', JOBS=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
