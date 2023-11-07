from config import marketClient, db_connection
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

# grab stock data from DB
cursor = db_connection.cursor()
cursor.execute("""
    SELECT id, symbol, name FROM stock
""")
rows = cursor.fetchall()

# create reference objects
symbols = [row['symbol'] for row in rows]
stock_dict = {}

# populate objects with fetched DB data
for row in rows:
    symbol = row['symbol']
    symbols.append(symbol)
    stock_dict[symbol] = row['id']


# API is limited to 200 symbols at a time
chunk_size = 200

# paginated for loop, requests 200 symbols at a time
for i in range(0, len(symbols), chunk_size):
    symbol_chunk = symbols[i:i+chunk_size]

    request_params = StockBarsRequest(
    symbol_or_symbols=symbol_chunk,
    start=datetime.strptime("2023-10-01", '%Y-%m-%d'),
    timeframe=TimeFrame.Day
)
    # make the request
    barsets = marketClient.get_stock_bars(request_params)
    print(f"processing chunk {i+chunk_size} of {len(symbols)}")

    # loop over the keys in the barsets dictionary
    for symbol in barsets.data:
    #loop through each bar for current symbol
        for bar in barsets[symbol]:
            stock_id = stock_dict[symbol]
            cursor.execute("""
                INSERT INTO stock_price (stock_id, date, open, high, low, close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (stock_id, bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume))

db_connection.commit()