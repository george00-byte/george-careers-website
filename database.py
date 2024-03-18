import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://george:ridealong@localhost:3306/comradecarees?charset=utf8mb4"

try:
  engine = create_engine(db_connection_string,
                         connect_args={"ssl": {
                             "ssl_ca": "/etc/ssl/cert.pem"
                         }})

  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = []
    for row in result.all():
      result_dicts.append(dict(row))

    print("Query executed successfully.")
    print("Result:", result_dicts)

except Exception as e:
  print("An error occurred:", e)
