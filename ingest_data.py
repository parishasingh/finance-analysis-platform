import yfinance as yf

#1. Choose the stocks we want to track (Tickers)
tickers = ["AAPL","MSFT","GOOGL"]

#2. Download the data from Yahoo Finance
#We are getting the last one year of daily data
data = yf.download(tickers,start="2025-01-01",end="2026-10-05")

#3. Print the first five rows to see what it looks like
print(data.head())

#4. Save this raw data to a csv file
data.to_csv("raw_stock_data.csv")
print("\nData successfully saved to raw_stock_data.csv")