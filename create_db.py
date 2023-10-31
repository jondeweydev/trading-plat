import sqlite3
import os

# get local dir
script_dir = os.path.dirname(os.path.abspath(__file__))
# set dir of db to current dir
db_path = os.path.join(script_dir, "app.db")
# establish DB
connection = sqlite3.connect(db_path)

# create cursor
cursor = connection.cursor()
# get schema path from current dir
schema_file_path = os.path.join(script_dir, 'schema.sql')

# read sql file
with open(schema_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

# execute queries from sql file
cursor.executescript(sql_script)
# commit to db
connection.commit()
