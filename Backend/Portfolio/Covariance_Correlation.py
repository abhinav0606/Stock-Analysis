import pandas as pd
import pandas_datareader.data as dt
import numpy as np
def cov_corr(company,weightage):
    dataframe=pd.DataFrame()
    for i in company:
        dataframe[i]=dt.DataReader(i,data_source="yahoo",start="2010-1-1")["Adj Close"]
    log_return=np.log(dataframe/dataframe.shift(1))
    weight=np.array(weightage)
    variance_of_port=np.dot(weight.T,np.dot(log_return.cov()*250,weight))
    # print(variance_of_port)
    # volatility
    # print(variance_of_port**0.5)
    return {"Variance_Portfolio":variance_of_port,"Volatility_Portfolio":variance_of_port**0.5}
