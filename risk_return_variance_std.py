import pandas as pd
from pandas_datareader import data as dt
import numpy as np
import matplotlib.pyplot as plt
company=["RELIANCE.NS","MRF.NS"]
dataframe=pd.DataFrame()
for i in company:
    dataframe[i]=dt.DataReader(i,data_source="yahoo",start="2010-1-1")["Adj Close"]
log_return=np.log(dataframe/dataframe.shift(1))
plt.plot(log_return)
plt.show()
print(log_return["RELIANCE.NS"].mean()*250*100)
print((log_return["RELIANCE.NS"].mean()))
print(((log_return["RELIANCE.NS"].mean()).std()*250)**0.5)