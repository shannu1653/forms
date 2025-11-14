import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env

conn = pymysql.connect(
    host=os.environ.get("MYSQL_HOST"),
    user=os.environ.get("MYSQL_USER"),
    password=os.environ.get("MYSQL_PASSWORD"),
    database=os.environ.get("MYSQL_DB"),
    port=int(os.environ.get("MYSQL_PORT")),
)
print("Connected successfully!")
conn.close()
