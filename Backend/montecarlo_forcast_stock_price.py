import numpy as np
import pandas as pd
from pandas_datareader import data as dt
import matplotlib.pyplot as plt
from scipy.stats import norm
import io
import base64
import urllib
def montecarloforcast(company):
    data=pd.DataFrame()
    data[company]=dt.DataReader(company,data_source="yahoo",start="2010-1-1")["Adj Close"]
    log_return=np.log(data/data.shift(1))
    data.plot(figsize=(10,10))
    log_return.plot(figsize=(10,10))
    plt.show()
    # calculate the mean and variance
    mean_return=log_return.mean()
    variance_return=log_return.var()
    # calculating drift
    drift=mean_return-(0.5*variance_return)
    drift=drift[company]
    # standard deviation
    return_deviation=log_return.std()
    return_deviation=return_deviation[company]
    # calculating the norms and the exponential part
    norming=norm.ppf(0.95)
    time_interval=1000#no of days for stock price
    iteration=10
    x=np.random.rand(10,2)
    exponential=np.exp(drift[company]+(return_deviation[company]*norm.ppf(np.random.rand(time_interval,iteration))))
    exponentially=exponential
    # calculating the next price
    previous_price=data.iloc[-1]
    Previous_price=previous_price
    price_list=np.zeros_like(exponential)
    price_list[0]=previous_price
    for i in range(1,time_interval):
        price_list[i]=price_list[i-1]*exponential[i]
    Price_List=price_list
    plt.title("Prediction")
    plt.figure(figsize=(10,10))
    plt.plot(price_list)
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    D={"Plot":uri,"Price_List":Price_List,"Previous_List":Previous_price,"Exponential":exponentially,
       "Norm":norming,"Return_Dev":return_deviation,"Drift":drift,"Mean_Return":mean_return,"Variance_return":variance_return}
    return D