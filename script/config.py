import os
from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient

import sqlite3
from dotenv import load_dotenv
load_dotenv()

# grab env vars
key = os.environ.get('ALPACA_KEY')
secret = os.environ.get('ALPACA_SECRET')

# connect to alpaca API
tradeAPI = TradingClient(api_key=key, secret_key=secret, url_override='https://api.alpaca.markets')

# client to pull market data
marketClient = StockHistoricalDataClient(api_key=key, secret_key=secret, url_override='https://api.alpaca.markets')

# establish dir constants
parent_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(parent_dir, "..", "db", "app.db")
schema_path = os.path.join(parent_dir, "..", "db", "schema.sql")

# connect to DB
db_connection = sqlite3.connect(db_path)