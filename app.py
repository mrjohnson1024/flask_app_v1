import os
from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db, load_jobs_with_select

app = Flask(__name__)


@app.route("/")
def something():
  jobs = load_jobs_from_db()
  return render_template('home.html', items=jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not found", 404
  return render_template('jobpage.html', job=job)


@app.route("/api/job/<id>")
def api_show_job(id):
  job = load_job_from_db(id)
  return jsonify(job)


@app.route("/api/jobs")
def api_show_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
