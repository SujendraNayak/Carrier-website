from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

# ✅ Create SQLAlchemy engine
engine = create_engine("mysql+pymysql://root:Sujendra%4027@127.0.0.1:3306/career")

# ✅ Function to load jobs from DB
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = [dict(row._mapping) for row in result.all()]
    return jobs

@app.route('/')
def home():
    jobs = load_jobs_from_db()   # get jobs from DB
    return render_template('home.html', JOBS=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()   # get jobs from DB
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
