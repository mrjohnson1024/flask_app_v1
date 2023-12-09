import os
from flask import Flask, render_template, jsonify
from db import engine, text

app = Flask(__name__)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


@app.route("/")
def something():
  jobs = load_jobs_from_db()
  return render_template('home.html', items=jobs)


@app.route("/api")
def list_LIST():
  return jsonify(LIST)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
