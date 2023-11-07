import sqlite3
import config


# set querying type to row object
config.db_connection.row_factory = sqlite3.Row
# setup cursor
cursor = config.db_connection.cursor()

# query select rows
cursor.execute("""
    SELECT symbol, name FROM stock
""")

# grab all rows from cursor
rows = cursor.fetchall()

symbols = [row['symbol'] for row in rows]

# grab alpaca data
assets = config.tradeAPI.get_all_assets()

# add only active and tradable assets to local db
# functionality for new symbols
for asset in assets:
    try:
        if asset.status == "active" and asset.tradable and asset.symbol not in symbols:
            print(f"Added a new stock {asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol, name) VALUES (?, ?)", 
                           (asset.symbol, asset.name))
    except Exception as e:
        print(e)

# commit to db
config.db_connection.commit()


