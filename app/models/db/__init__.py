import urllib
from app.config import *
from app.libs.db.sql_uteis import DbSqlA

try:
  sql_server = DbSqlA(f"mssql+pyodbc://{USER}:{urllib.parse.quote_plus(PASSWORD)}@{SERVER}/{DB}?driver={DRIVER}")
except Exception as e:
  print(e)
