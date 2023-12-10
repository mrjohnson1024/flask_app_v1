import os
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, VARCHAR, text, select

# Collect our vars from secrets manager
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PWD']
db_uri = os.environ['DB_URI']
db_default = "flask_app_v1"

metadata = MetaData()

# Instantiate the database connection
engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_pass}@{db_uri}/{db_default}",
    connect_args={"ssl": {
        "ca": "/etc/ssl/certs/ca-certificates.crt",
    }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_jobs_with_select():
  with engine.connect() as conn:
    stmt = select(jobs_table).where(
        jobs_table.columns.location == 'Chicago, IL')
    result = conn.execute(stmt).fetchall()
    return result


jobs_table = Table('jobs', metadata,
                   Column("id", Integer, autoincrement=True, primary_key=True),
                   Column("title", VARCHAR(50)), Column("location", Integer),
                   Column("salary", Integer), Column("currency", String(4)),
                   Column("responsibilities", VARCHAR(2000)),
                   Column("requirements", VARCHAR(2000)))
