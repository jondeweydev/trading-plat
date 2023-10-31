import sqlite3
import config

# create cursor
cursor = config.connection.cursor()

# read sql file
with open(config.schema_path, 'r') as sql_file:
    sql_script = sql_file.read()

# execute queries from sql file
cursor.executescript(sql_script)
# commit to db
config.connection.commit()
