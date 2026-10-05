import pandas as pd
import matplotlib.pyplot as plt

#1. Load the clean data
df = pd.read_csv("clean_stock_data.csv")

#2. Pivote the data so we have Dates as rows and Trickers as columns
#This makes it easier to plot
pivot_df = df.pivot(index='Date',columns='Ticker',values='Close')

#3. Create a simple line Chart
pivot_df.plot(figsize=(10,6))
plt.title("Stock Closing Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price($)")
plt.grid(True)

#4. Save the chart as an image and show it
plt.savefig("stock_prices_chart.png")
print("Success! Chart saved as stock_prices_chart.png")
plt.show()
