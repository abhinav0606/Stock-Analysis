import numpy as np
import pandas as pd
from pandas_datareader import data as dt
from scipy.stats import norm
import matplotlib.pyplot as plt
company="PG"
data=pd.DataFrame()
data[company]=dt.DataReader(company,data_source="yahoo",start="1995-1-1")["Adj Close"]
log_return=np.log(data/data.shift(1))
T=1.0
r=0.025
t_interval=250
delta_t=T/t_interval
iteration=10000
std=(data.std()*250)**0.5
std=std.values
Z=np.random.standard_normal((t_interval+1,iteration))
s=np.zeros_like(Z)
s[0]=data.iloc[-1]
print(s[0])
for i in range(1,t_interval+1):
    s[i]=s[i-1]*np.exp((r-std**0.5*0.5)*delta_t+std*delta_t**0.5*Z[i])
print(s)
plt.figure(figsize=(10,10))
plt.plot(s)
plt.show()