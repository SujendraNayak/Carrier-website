from flask import Flask, render_template, jsonify
app=Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'New York, NY',
        'salary': '$120,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, CA',
        'salary': '$150,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Austin, TX',
        'salary': '$130,000'
    },
      {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'New York, NY',
        'salary': '$120,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'San Francisco, CA',
        'salary': '$150,000'
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Austin, TX',
        'salary': '$130,000'
    }
]
@app.route('/')
def home():
    return render_template('home.html',JOBS=JOBS)

@app.route('/api/JOBS')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)