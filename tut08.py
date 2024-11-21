import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from datetime import datetime
%matplotlib inline

#1)
df = pd.read_csv('/content/infy_stock.csv')
df.head(10)
df.info()
df.isnull().sum()
df.dropna(axis=0,inplace=True)
df.info()

#2)
plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['Close'], label='Closing Price')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Price Over Time')
plt.legend()
plt.show()


fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show()

#3)
# Daily Return Average
df['Daily_Return']=((df['Close'] - df['Open']) / df['Open'])*100

average_return = df['Daily_Return'].mean()
median_return = df['Daily_Return'].median()

print('Average Daily Return:', average_return)
print('Median Daily Return:', median_return)

std_dev_close = df['Close'].std()
print('Standard Deviation:', std_dev_close)

#4)
# Calculate 50-day and 200-day moving averages
df['50-day MA'] = df['Close'].rolling(window=50).mean()
df['200-day MA'] = df['Close'].rolling(window=200).mean()

#5)
# Plot moving averages
plt.figure(figsize=(14,8))
plt.plot(df['Close'], label='Closing Price')
plt.plot(df['50-day MA'], label='50-Day MA', color='orange')
plt.plot(df['200-day MA'], label='200-Day MA', color='green')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('50-day and 200-day Moving Averages')
plt.legend()
plt.show()

years = df['Year'].unique()

#6)
# Identifying bullish and bearish trends based on moving averages
df['Trend'] = np.where(df['50-day MA'] > df['200-day MA'], 'Bullish', 'Bearish')

# Marking trends on the plot
plt.figure(figsize=(14,8))
plt.plot(df['Close'], label='Closing Price')
plt.plot(df['50-day MA'], label='50-Day MA', color='orange')
plt.plot(df['200-day MA'], label='200-Day MA', color='green')

# Highlight bullish and bearish trends
bullish = df[df['Trend'] == 'Bullish']
bearish = df[df['Trend'] == 'Bearish']
plt.fill_between(df.index, df['Close'], where=df['50-day MA'] > df['200-day MA'], color='green', alpha=0.3, label='Bullish')
plt.fill_between(df.index, df['Close'], where=df['50-day MA'] < df['200-day MA'], color='red', alpha=0.3, label='Bearish')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Bullish and Bearish Trends')
plt.legend()
plt.show()