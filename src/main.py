import sqlite3
import os

# get this dir
script_dir = os.path.dirname(os.path.abspath(__file__))
# set dir of db to this folder
db_path = os.path.join(script_dir, "..", "db", "app.db")
# establish DB
connection = sqlite3.connect(db_path)
# setup cursor
cursor = connection.cursor()

# select rows
cursor.execute("""
    SELECT symbol, company FROM stock
""")
# grab all rows from cursor
rows = cursor.fetchall()

# test
for row in rows:
    print(row)

