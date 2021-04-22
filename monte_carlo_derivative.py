import pandas as pd
import numpy as np
from pandas_datareader import data as dt
import matplotlib.pyplot as plt
from scipy.stats import norm
# calculating the black scholes formula and getting the call value
def d1(S,K,r,std,T):
    return (np.log(S/K)+((r+((std**2)/2))*T))/(std*np.sqrt(T))
def d2(S,K,r,std,T):
    return (np.log(S / K) + ((r - ((std ** 2) / 2)) * T)) / (std * np.sqrt(T))
def BSF(S,K,r,std,T):
    return (S*norm.cdf(d1(S,K,r,std,T)))-((K*np.exp(-r*T))*norm.cdf(d2(S,K,r,std,T)))
company="PG"
data=pd.DataFrame()
data[company]=dt.DataReader(company,data_source="yahoo",start="1995-1-1",end="2017-3-21")["Adj Close"]
log_return=np.log(data/data.shift(1))
S=data.iloc[-1]
std=(log_return.std()*250)**0.5
r=0.025
K=110
T=1
print(d1(S,K,r,std,T))
print(d2(S,K,r,std,T))
print(BSF(S,K,r,std,T))
print(S)