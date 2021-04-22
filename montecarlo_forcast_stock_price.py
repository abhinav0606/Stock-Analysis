import numpy as np
import pandas as pd
from pandas_datareader import data as dt
import matplotlib.pyplot as plt
from scipy.stats import norm
company="RELIANCE.NS"
data=pd.DataFrame()
data[company]=dt.DataReader(company,data_source="yahoo",start="1995-1-1")["Adj Close"]
log_return=np.log(data/data.shift(1))
print(log_return.tail())
data.plot(figsize=(10,10))
log_return.plot(figsize=(10,10))
plt.show()
# calculate the mean and variance
mean_return=log_return.mean()
variance_return=log_return.var()
# calculating drift
drift=mean_return-(0.5*variance_return)
print(drift[company])
# standard deviation
return_deviation=log_return.std()
print(return_deviation[company])
# calculating the norms and the exponential part
print(norm.ppf(0.95))
time_interval=1000#no of days for stock price
iteration=10
x=np.random.rand(10,2)
print(x)
exponential=np.exp(drift[company]+(return_deviation[company]*norm.ppf(np.random.rand(time_interval,iteration))))
print("----------------------------------------")
print(exponential)
# calculating the next price
previous_price=data.iloc[-1]
print(previous_price)
price_list=np.zeros_like(exponential)
price_list[0]=previous_price
print(price_list)
for i in range(1,time_interval):
    price_list[i]=price_list[i-1]*exponential[i]
print(price_list)
plt.figure(figsize=(10,10))
plt.plot(price_list)
plt.show()