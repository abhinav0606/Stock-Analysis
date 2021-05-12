from pandas_datareader import data as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import urllib
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
import datetime
def prediction(name):
    number=21
    Scaler=MinMaxScaler(feature_range=(0,1))
    dataset=dt.DataReader(name,data_source="yahoo",start="2010-1-1")
    dataset.index=pd.to_datetime(dataset.index,format="%Y-%m-%d")
    dataframe=pd.DataFrame(index=range(len(dataset)),columns=["Date","Close"])
    for i in range(len(dataset)):
        dataframe["Date"][i]=list(dataset.index)[i]
        dataframe["Close"][i]=dataset["Close"][i]
    dataframe["Date"]=pd.to_datetime(dataframe.Date,format="%Y-%m-%d")
    dataframe.index=dataframe.Date
    dataframe.drop("Date",axis=1,inplace=True)
    valued_data=dataframe.values
    training=valued_data[:2089,:]
    testing=valued_data[2089:,:]
    scaled_data=Scaler.fit_transform(valued_data)
    x_train,x_test,y_test,y_train=[],[],[],[]
    for i in range(number,len(training)):
        x_train.append(scaled_data[i-number:i,0])
        y_train.append(scaled_data[i,0])
    for i in range(len(training),len(dataframe)):
        x_test.append(scaled_data[i-number:i,0])
        y_test.append(scaled_data[i,0])
    x_train,y_train,x_test,y_test=np.array(x_train),np.array(y_train),np.array(x_test),np.array(y_test)
    mlr=LinearRegression()
    mlr.fit(x_train,y_train)
    training=dataframe[:2089]
    testing=dataframe[2089:]
    testing["Prediction"]=Scaler.inverse_transform(mlr.predict(x_test).reshape(-1,1))
    plt.figure(3)
    plt.clf()
    plt.title("Model Prediction")
    plt.plot(training["Close"],label="Training Data")
    plt.plot(testing["Close"],label="Testing Date")
    plt.plot(testing["Prediction"],label="Predicted Date")
    plt.legend()
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri1=urllib.parse.quote(string)
    # future_prediction
    prediction_list = []
    prediction = scaled_data[len(dataframe) - (number + 1):len(dataframe) - 1, 0]
    prediction_list.append(prediction)
    Previous_day=(Scaler.inverse_transform(mlr.predict(prediction_list).reshape(-1, 1)))[0][0]
    prediction_list = []
    prediction = scaled_data[len(dataframe) - (number):len(dataframe), 0]
    prediction_list.append(prediction)
    Todays=(Scaler.inverse_transform(mlr.predict(prediction_list).reshape(-1, 1)))[0][0]
    main_list = []
    for i in range(number):
        prediction_list = []
        prediction = list(scaled_data[len(dataframe) - number + i:, 0])
        if main_list == []:
            pass
        else:
            for i in main_list:
                prediction.append(i)
        prediction_list.append(prediction)
        main_list.append(mlr.predict(prediction_list))
    l = list(Scaler.inverse_transform(main_list))
    p = []
    for i in l:
        p.append(round(i[0], 2))
    Data_frame = pd.DataFrame(index=range(len(p)), columns=["Prediction"])
    for i in range(len(p)):
        Data_frame["Prediction"][i] = int(p[i])
    plt.figure(4)
    plt.clf()
    plt.title(f"Future {number} Days prediction for {name.split('.')[0]} Stock-MLR")
    plt.plot(Data_frame["Prediction"])
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri2=urllib.parse.quote(string)
    plt.figure(5)
    plt.clf()
    todays_date = datetime.datetime.now().date()
    index = pd.date_range(todays_date, periods=number, freq='D')
    df = pd.DataFrame(index=index, columns=["Prediction"])
    for i in range(len(p)):
        df["Prediction"][i] = p[i]
    plt.title("Overall Figure-MLR")
    plt.plot(training["Close"], label="Actuall")
    plt.plot(testing["Close"], label="Actuall Testing")
    plt.plot(testing["Prediction"], label="Test Prediction")
    plt.plot(df["Prediction"], label="Future")
    plt.legend()
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri3=urllib.parse.quote(string)
    plt.figure(6)
    plt.clf()
    plt.title("MLR")
    plt.plot(testing["Close"], label="Actuall Testing")
    plt.plot(testing["Prediction"], label="Test Prediction")
    plt.plot(df["Prediction"], label="Future")
    plt.legend()
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri4=urllib.parse.quote(string)
    D={}
    D["Previous"]=Previous_day
    D["Today"]=Todays
    D["Plot1"]=uri1
    D["Plot2"] =uri2
    D["Plot3"] =uri3
    D["Plot4"] =uri4
    d={}
    for i in list(df.index):
        d[str(i).split(" ")[0]]=df["Prediction"][i]
    D["Upcoming_Pred"] = d
    return D