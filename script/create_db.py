import sqlite3
import os
import config

# connect to DB
connection = sqlite3.connect(config.db_path)
# create cursor
cursor = connection.cursor()

# read sql file
with open(config.schema_path, 'r') as sql_file:
    sql_script = sql_file.read()

# execute queries from sql file
cursor.executescript(sql_script)
# commit to db
connection.commit()
