import sqlite3
import config


# set querying type to row object
config.connection.row_factory = sqlite3.Row
# setup cursor
cursor = config.connection.cursor()

# query select rows
cursor.execute("""
    SELECT symbol, company FROM stock
""")

# grab all rows from cursor
rows = cursor.fetchall()

symbols = [row['symbol'] for row in rows]

# grab alpaca data
assets = config.api.get_all_assets()

# add only active and tradable assets to local db
# functionality for new symbols
for asset in assets:
    try:
        if asset.status == "active" and asset.tradable and asset.symbol not in symbols:
            print(f"Added a new stock {asset.symbol} {asset.name}")
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", 
                           (asset.symbol, asset.name))
    except Exception as e:
        print(e)

# commit to db
config.connection.commit()


