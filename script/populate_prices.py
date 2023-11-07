from config import marketClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime


request_params = StockBarsRequest(
    symbol_or_symbols=["AAPL", "MSFT"],
    timeframe=TimeFrame.Day,
    start=datetime.strptime("2023-10-01", '%Y-%m-%d')
)

bars = marketClient.get_stock_bars(request_params)

print(bars)