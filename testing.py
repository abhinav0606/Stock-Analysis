# testing
from pandas_datareader import data as dt
import pandas as pd
data=dt.DataReader("RELIANCE.NS",data_source="yahoo",start="2018-1-1")
data["Simple Return"]=(data['Adj Close']/data["Adj Close"].shift(1))-1
print(data)
import matplotlib.pyplot as plt
import seaborn as sb
sb.set()
plt.xlabel("Days")
plt.ylabel("Price in Rupee")
plt.plot(data['Simple Return'])
plt.show()