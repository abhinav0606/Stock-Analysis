import pandas as pd
from pandas_datareader import data as dt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import datetime
from sklearn.linear_model import LinearRegression
Scaler=MinMaxScaler(feature_range=(0,1))
company=input("Enter the name of the company")
number=int(input("Enter the number"))
dataset=dt.DataReader(company,data_source="yahoo",start="2010-1-1")
dataset.index=pd.to_datetime(dataset.index,format="%Y-%m-%d")
dataframe=pd.DataFrame(index=range(len(dataset)),columns=["Date","Open"])
for i in range(len(dataset)):
    dataframe["Date"][i]=list(dataset.index)[i]
    dataframe["Open"][i]=dataset["Open"][i]
dataframe["Date"]=pd.to_datetime(dataframe.Date,format="%Y-%m-%d")
dataframe.index=dataframe.Date
dataframe.drop("Date",axis=1,inplace=True)
valued_data=dataframe.values
train=valued_data[:2089,:]
test=valued_data[2089:,:]
x_train,y_train=[],[]
x_test,y_test=[],[]
scaled_data=Scaler.fit_transform(valued_data)
# print(dataset["Close"].values.reshape(-1,1))
# print(valued_data)
close_value=Scaler.transform(dataset["Close"].values.reshape(-1,1))
for i in range(number,len(train)):
    x_train.append(scaled_data[i-number:i,0])
    y_train.append(close_value[i,0])
for i in range(len(train),len(dataframe)):
    x_test.append(scaled_data[i-number:i,0])
    y_test.append(close_value[i,0])
x_train,y_train=np.array(x_train),np.array(y_train)
x_test,y_test=np.array(x_test),np.array(y_test)
mlr=LinearRegression()
mlr.fit(x_train,y_train)
train=dataframe[:2089]
test=dataframe[2089:]
# print(mlr.predict(x_test))
print(Scaler.inverse_transform(mlr.predict(x_test).reshape(-1,1)))
test["Prediction"]=Scaler.inverse_transform(mlr.predict(x_test).reshape(-1,1))
plt.figure(1)
# plt.plot(train["Open"],label="Training")
plt.plot(test["Open"],label="Testing")
plt.plot(test["Prediction"],label="Prediction")
plt.legend()
plt.show()