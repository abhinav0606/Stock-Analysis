# looking into adj close
import pandas as pd
from pandas_datareader import data as dt
import numpy as np
import matplotlib.pyplot as plt
portfolio=["RELIANCE.NS","MRF.NS"]
weights=[0.75,0.25]
dataframe=pd.DataFrame()
for i in portfolio:
    dataframe[i]=dt.DataReader(i,data_source="yahoo",start="2010-1-1")["Adj Close"]
normal_100=(dataframe/dataframe.iloc[0])*100
plt.plot(normal_100)
# plt.show()

weights=np.array(weights)
simple_return=(dataframe/dataframe.shift(1))-1
port_return=np.dot(simple_return,weights)*100

annual_return=simple_return.mean()*250
print(annual_return)
