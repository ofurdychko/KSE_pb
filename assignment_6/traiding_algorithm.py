import requests 
import pandas as pd

url = "https://api.binance.com/api/v3/klines"
params = {
    "symbol": "SOLUSDT",
    "interval": "1d",           
    "limit": 730    # 2 years, Binance API allows requesting up to 1000 days of historical data
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data, columns = ["open_time", "open", "high", "low", "close", "volume", 
                                   "close_time", "quote_asset_volume", "number_of_trades",
                                   "taker_buy_base_volume", "taker_buy_quote_volume", "ignore"]) 

df = df[["open", "close", "high", "low", "volume"]]

df = df.astype(float) # the values need to be converted from string to float data type

short = 5 # just an exapmle 
long = 25 # just an exapmle  
df["short_SMA"] = df["close"].rolling(window=short).mean() #SMA - Simple Moving Average
df["long_SMA"] = df["close"].rolling(window=long).mean()

df["operations"] = (df["short_SMA"] > df["long_SMA"]).astype(int)
df["operations_shifted"] = df["operations"].shift(1).fillna(0).astype(int) #.fillna(0).astype(int) - for value = 0, not 0.0

df["trades"] = "Hold"
df.loc[(df["operations"] == 1) & (df["operations_shifted"] == 0), "trades"] = "Buy" # df.loc[condition, "column"] = value
df.loc[(df["operations"] == 0) & (df["operations_shifted"] == 1), "trades"] = "Sell"

total_profit = 0 # our profit
token_price = 0 

for i in range(len(df)):
    if df.loc[i,"trades"]=="Buy":
        token_price = df.loc[i, "close"]
    elif df.loc[i, "trades"] == "Sell":
        profit = df.loc[i, "close"] - token_price
        total_profit += profit
        df.loc[i, "profit"] = profit # for the column "profit"
        token_price = 0

a = int(total_profit) # just for clarity:
df = df[["open","close","high","low","volume","trades","profit"]] # just for clarity:

print(f"Your profit: {a}$")
print(df.fillna("-"))

