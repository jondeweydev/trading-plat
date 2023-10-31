import sqlite3
import os

# get local dir
script_dir = os.path.dirname(os.path.abspath(__file__))
# set dir of db to outside folder
db_path = os.path.join(script_dir, "..", "db", "app.db")
# establish DB
connection = sqlite3.connect(db_path)

# create cursor
cursor = connection.cursor()
# get schema path from outside dir
schema_file_path = os.path.join(script_dir, "..", "db", "schema.sql")

# read sql file
with open(schema_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# execute queries from sql file
cursor.executescript(sql_script)
# commit to db
connection.commit()
