import pandas as pd

#1. Load the raw data
#We use headers=[0,1] to handle the two leves of column headers
df = pd.read_csv("raw_stock_data.csv",header=[0,1],index_col=0)

#2. Reshape the data
#We move the ticker symbols (AAPL,MSFT,GOOGL) into their own column
df = df.stack(level=1).reset_index()

#3. Rename the columns to be clean and simple
df.columns = ['Date', 'Ticker', 'Close', 'High', 'Low', 'Open', 'Volume']

#4. Sort the data by Data and Ticker
df = df.sort_values(by=['Date','Ticker'])

#5. Save the cean file
df.to_csv("clean_stock_data.csv",index=False)
print("Success! Data transformed and saved as clean_stock_data.csv")
print(df.head())
