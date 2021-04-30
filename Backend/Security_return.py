from pandas_datareader import data as dt
import matplotlib.pyplot as plt
import io
import urllib
import base64
def simple_return(name):
    data=dt.DataReader(name,data_source="yahoo",start="1995-1-1")
    data["Simple Return"]=(data["Adj Close"]/data["Adj Close"].shift(1))-1
    plt.title("Simple Return")
    plt.plot(data["Simple Return"])
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    overall_mean=(data["Simple Return"].mean()*250*100)
    return {"Overall_Mean":overall_mean,"Plot":uri}