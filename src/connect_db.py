import os
import snowflake.connector

con = snowflake.connector.connect(
    user=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD') + '>&B~HG',
    account=os.getenv('ACCOUNT'),
    warehouse='COMPUTH_WH',
    database=os.getenv('DATABASE'),
    schema=os.getenv('SCHEMA'),
)

con.cursor().execute('CREATE TABLE IF NOT EXISTS SAMPLE_DATA')



