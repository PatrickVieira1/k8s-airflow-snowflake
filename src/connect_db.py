import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

con = snowflake.connector.connect(
    user=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
    account=os.getenv('ACCOUNT'),
    warehouse='COMPUTE_WH',
    database=os.getenv('DATABASE'),
    schema=os.getenv('SCHEMA'),
)


query = """ INSERT INTO SAMPLE_DATA (name, created, status)
VALUES ('Joao Kuberlitos', CURRENT_TIMESTAMP, TRUE);
  """

try:
    con.cursor().execute(query)
    con.commit()
except snowflake.connector.Error as e:
    print("Snowflake error:", e)

