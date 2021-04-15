import pandas as pd
import pandas_datareader.data as dt
import matplotlib.pyplot as plt
import numpy as np
company=["RELIANCE.NS","TCS.NS"]
dataframe=pd.DataFrame()
for i in company:
    dataframe[i]=dt.DataReader(i,data_source="yahoo",start="2010-1-1")["Adj Close"]
log_return=np.log(dataframe/dataframe.shift(1))
print(log_return)
print("---------")
print(log_return.mean()*250)
print("---------")
print(log_return.std()*250)
print("-----------")
print(log_return.var()*250)
print("-----------")
print(log_return.cov())
print("---------")
print(log_return.corr())


weight=[0.5,0.5]
weight=np.array(weight)
variance_of_port=np.dot(weight.T,np.dot(log_return.cov()*250,weight))
print(variance_of_port)
# volatility
print(variance_of_port**0.5)