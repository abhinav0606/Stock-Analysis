import numpy as np
import pandas as pd
from pandas_datareader import data as dt
# here company is PG and the global market is ^GSPC
company=["PG","^GSPC"]
my_data=pd.DataFrame()
for i in company:
    my_data[i]=dt.DataReader(i,data_source="yahoo",start="2015-1-1",end="2020-1-1")["Adj Close"]
print(my_data.tail())
print(my_data.head())
log_return=np.log(my_data/my_data.shift(1))
cov_market=(log_return.cov()*250).iloc[0,1]
print(cov_market)
variance_market=log_return["^GSPC"].var()*250
print(variance_market)

beta=cov_market/variance_market
print(beta)
# stock return
return_expected=0.0073+(beta*0.05)
print(return_expected)