import sqlite3
import os
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

load_dotenv()

# grab env vars
key = os.environ.get('ALPACA_KEY')
secret = os.environ.get('ALPACA_SECRET')

# connect to alpaca API
api = TradingClient(api_key=key, secret_key=secret, url_override='https://api.alpaca.markets')

# get this dir
script_dir = os.path.dirname(os.path.abspath(__file__))

# set dir of db to this folder
db_path = os.path.join(script_dir, "app.db")
# establish DB
connection = sqlite3.connect(db_path)
# setup cursor
cursor = connection.cursor()

# grab alpaca data
assets = api.get_all_assets()

# add only active and tradable assets to local db
for asset in assets:
    try:
        if asset.status == "active" and asset.tradable:
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    except Exception as e:
        print(e)

# commit to db
connection.commit()


