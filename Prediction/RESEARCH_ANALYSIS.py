import pandas as pd
import pandas_datareader.data as dt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import datetime
from sklearn.linear_model import LinearRegression
Scaler=MinMaxScaler(feature_range=(0,1))
listy=[7,11,15,20,21,25,30,33,35,40,45,50,51,55,60,63,70,77,75,80,81,83,90,93,95,99,100]
company=input("Enter the code of the company")
dataset=dt.DataReader(company,data_source="yahoo",start="2010-1-1")
dataset.index=pd.to_datetime(dataset.index,format="%Y-%m-%d")
dataframe=pd.DataFrame(index=range(len(dataset)),columns=["Date","Close"])
for i in range(len(dataset)):
    dataframe["Date"][i]=list(dataset.index)[i]
    dataframe["Close"][i]=dataset["Close"][i]
dataframe["Date"]=pd.to_datetime(dataframe.Date,format="%Y-%m-%d")
dataframe.index=dataframe.Date
dataframe.drop("Date",axis=1,inplace=True)
valued_data=dataframe.values
scaled_data=Scaler.fit_transform(valued_data)
train=valued_data[:2089,:]
test=valued_data[2089:,:]
for number in listy:
    x_train,y_train=[],[]
    for i in range(number,len(train)):
        x_train.append(scaled_data[i-number:i,0])
        y_train.append(scaled_data[i,0])
    x_train,y_train=np.array(x_train),np.array(y_train)
    x_test,y_test=[],[]
    for i in range(len(train),len(dataframe)):
        x_test.append(scaled_data[i-number:i,0])
        y_test.append(scaled_data[i,0])
    x_test,y_test=np.array(x_test),np.array(y_test)
    mlr=LinearRegression()
    mlr.fit(x_train,y_train)
    print("--------------------------------------------------------------")
    print("For Number of days = "+str(number))
    prediction_list = []
    prediction = scaled_data[len(dataframe) - (number + 1):len(dataframe) - 1, 0]
    prediction_list.append(prediction)
    print(Scaler.inverse_transform(mlr.predict(prediction_list).reshape(-1, 1)))
    prediction_list = []
    prediction = scaled_data[len(dataframe) - (number):len(dataframe), 0]
    prediction_list.append(prediction)
    print(Scaler.inverse_transform(mlr.predict(prediction_list).reshape(-1, 1)))
    print("--------------------------------------------------------------")