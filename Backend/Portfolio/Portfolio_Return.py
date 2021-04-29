import pandas as pd
from pandas_datareader import data as dt
import numpy as np
import matplotlib.pyplot as plt
import urllib
import base64
import io
def port_return(company,weightage):
    dataframe=pd.DataFrame()
    for i in company:
        dataframe[i]=dt.DataReader(i,data_source="yahoo",start="2010-1-1")["Adj Close"]
    normal_100=(dataframe/dataframe.iloc[0])*100
    plt.title("Normal 100")
    for i in company:
        plt.plot(normal_100[i],label=i)
    plt.legend()
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    weights=np.array(weightage)
    simple_return=(dataframe/dataframe.shift(1))-1
    port_return=np.dot(simple_return,weights)*100
    annual_return=simple_return.mean()*250
    return {"Annual_Return":annual_return,"Portfolio_return":port_return,"Normal_100_plot":uri}
port_return(["RELIANCE.NS","TCS.NS"],[0.5,0.5])