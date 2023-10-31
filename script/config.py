import os

parent_dir = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(parent_dir, "..", "db", "app.db")
schema_path = os.path.join(parent_dir, "..", "db", "schema.sql")