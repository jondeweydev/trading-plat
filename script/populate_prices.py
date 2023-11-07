from config import marketClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

request_params = StockBarsRequest(
    symbol_or_symbols=["Z"],
    start=datetime.strptime("2023-10-01", '%Y-%m-%d'),
    timeframe=TimeFrame.Minute
)

barsets = marketClient.get_stock_bars(request_params)

# print(barsets.data)

# loop over the keys in the barsets dictionary
for symbol in barsets.data:
    print(f"processing symbol {symbol}")

    #loop through each bar for current symbol
    for bar in barsets[symbol]:
        print(bar.timestamp, bar.open, bar.high, bar.low, bar.close, bar.volume)