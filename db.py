import os
import sqlalchemy
from sqlalchemy import create_engine, text, select

# Collect our vars from secrets manager
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PWD']
db_uri = os.environ['DB_URI']
db_default = "flask_app_v1"

# Instantiate the database connection
engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_pass}@{db_uri}/{db_default}",
    connect_args={"ssl": {
        "ca": "/etc/ssl/certs/ca-certificates.crt",
    }})

# Test connection by running a simple query
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())

  print(result_dicts)

# result_all = result.all()
# print(type(result_all[0]))
# first_result = result_all[0]._asdict()
# print(first_result)
