from pandas_datareader import data as dt
import numpy as np
import matplotlib.pyplot as plt
import urllib
import io
import base64
def log_return(name):
    data=dt.DataReader(name,data_source="yahoo",start="1995-1-1")
    data["Log Return"]=np.log(data["Adj Close"]/data["Adj Close"].shift(1))
    plt.figure(2)
    plt.clf()
    plt.title("Log Return")
    plt.plot(data["Log Return"])
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    overall_mean=(data["Log Return"].mean()*250*100)
    return {"Overall_Mean":overall_mean,"Plot":uri}