import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from pandas_datareader import data

start = datetime(2020, 1, 1)
end = datetime(2021, 2, 9)


plt.title('KOSPI index')
df = data.get_data_yahoo('^KS11', start, end) #pandas_datareader를 통해서 주식 데이터 가져옴 df = data frame
plt.plot(df['Adj Close'])

ymin = df['Adj Close'].min()
ymax = df['Adj Close'].max()

plt.ylim(ymin, ymax)
plt.fill_between(df.index, ymin, df['Adj Close'], alpha=0.5)
plt.xticks(rotation=30)
plt.show()