import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import yfinance as yf

instrument = 'TSLA'
start_date = '2022-01-01'
end_date = date.today()

stock = yf.download(instrument, start_date, end_date)

#print stock info
print(stock)

#print simple return and log return
log_returns = np.log(stock['Adj Close']).diff().sum()

simple_returns = stock['Adj Close'].pct_change().sum()

print(f'Log Returns: {log_returns}')

print(f'Simple Returns: {simple_returns}')
