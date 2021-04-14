import pandas as pd
from pandas_datareader import data as dt
import numpy as np
import matplotlib.pyplot as plt
name=input("Enter the NSE code of the Stock")
data=dt.DataReader(name,data_source="yahoo",start="1995-1-1")
data["Simple Return"]=(data["Adj Close"]/data["Adj Close"].shift(1))-1
plt.plot(data["Simple Return"])
plt.show()
overall_mean=(data["Simple Return"].mean()*250*100)
print(overall_mean)