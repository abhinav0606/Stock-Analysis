import io
import base64
import urllib
import numpy as np
import pandas as pd
from pandas_datareader import data as dt
import matplotlib.pyplot as plt
from scipy.stats import norm

def monte_forcast(company):
    d={}
    data=pd.DataFrame()
    data[company]=dt.DataReader(company,data_source="yahoo",start="1995-1-1")["Adj Close"]
    log_return=np.log(data/data.shift(1))
    # calculate the mean and variance
    mean_return=log_return.mean()
    variance_return=log_return.var()
    d["Mean_return"]=mean_return[company]
    d["Variance_return"]=variance_return[company]
    # calculating drift
    drift=mean_return-(0.5*variance_return)
    d["Drift"]=drift[company]
    # standard deviation
    return_deviation=log_return.std()
    d["Std_deviation"]=return_deviation[company]
    # calculating the norms and the exponential part
    d["Norm"]=norm.ppf(0.95)
    time_interval=1000#no of days for stock price
    iteration=10
    x=np.random.rand(10,2)
    exponential=np.exp(drift[company]+(return_deviation[company]*norm.ppf(np.random.rand(time_interval,iteration))))
    # calculating the next price
    previous_price=data.iloc[-1]
    price_list=np.zeros_like(exponential)
    price_list[0]=previous_price
    for i in range(1,time_interval):
        price_list[i]=price_list[i-1]*exponential[i]
    plt.figure(7)
    plt.clf()
    plt.title("Monte-Carlo Prediction Of 1000 Iterations")
    plt.plot(price_list)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    d["plot"]=uri
    return d
