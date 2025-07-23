import yfinance as yf
import mplfinance as mpf
import pandas as pd

# Download historical stock data
ticker = 'AAPL'
data = yf.download(ticker, start='2023-01-01', end='2024-01-01')

# Keep only necessary columns and drop rows with missing values
data = data[['Open', 'High', 'Low', 'Close', 'Volume']].dropna()

# Ensure all columns are float (except Volume which can be int or float)
data[['Open', 'High', 'Low', 'Close']] = data[['Open', 'High', 'Low', 'Close']].astype(float)

# Make sure the index is a DatetimeIndex (required by mplfinance)
if not isinstance(data.index, pd.DatetimeIndex):
    data.index = pd.to_datetime(data.index)

# Plot candlestick chart
mpf.plot(
    data,
    type='candle',
    style='charles',
    title=f'{ticker} Candlestick Chart',
    volume=True
)


