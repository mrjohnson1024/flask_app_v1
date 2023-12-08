import os
import sqlalchemy
from sqlalchemy import create_engine, text

# Collect our vars from secrets manager
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PWD']
db_uri = os.environ['DB_URI']
db_default = "flask_app_v1"

engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_pass}@{db_uri}/{db_default}",
    connect_args={"ssl": {
        "ca": "/etc/ssl/certs/ca-certificates.crt",
    }})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())
