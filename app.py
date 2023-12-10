import os
from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_jobs_with_select

app = Flask(__name__)


@app.route("/")
def something():
  jobs = load_jobs_from_db()
  return render_template('home.html', items=jobs)


@app.route("/api/jobs")
def list_LIST():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
