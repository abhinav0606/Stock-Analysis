import numpy as np
import pandas as pd
from pandas_datareader import data as dt
def beta(name):
    l=[]
    if ".NS" in name:
        l=[name,"^NSEI"]
    elif ".BO" in name:
        l=[name,"^BSESN"]
    else:
        l=[]
    my_data = pd.DataFrame()
    for i in l:
        my_data[i] = dt.DataReader(i, data_source="yahoo", start="2010-1-1")["Adj Close"]
    log_return = np.log(my_data / my_data.shift(1))
    cov_market = (log_return.cov() * 250).iloc[0, 1]
    Market_Covariance=(cov_market)
    variance_market = log_return[l[1]].var() * 250
    Market_Variance=variance_market
    beta = cov_market / variance_market
    Beta_Stock=(beta)
    volatility_of_stock=(Beta_Stock*100)-100
    D={"Cov Market wrt Stock":Market_Covariance,"Var Market":Market_Variance,"Beta":beta,"Volatility_of_stock":volatility_of_stock}
    return D
