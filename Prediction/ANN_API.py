import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as dt
from sklearn.preprocessing import MinMaxScaler
Scaler=MinMaxScaler(feature_range=(0,1))
import tensorflow as tf
import datetime
company=input("Enter the Company name")
number=int(input("Enter the number"))
dataset=dt.DataReader(company,data_source="yahoo",start="2010-1-1")
dataset.index=pd.to_datetime(dataset.index,format="%Y-%m-%d")
dataframe=pd.DataFrame(index=range(len(dataset)),columns=["Date","Close"])
for i in range(len(dataset)):
    dataframe["Date"][i]=list(dataset.index)[i]
    dataframe["Close"][i]=dataset["Close"][i]
dataframe["Date"]=pd.to_datetime(dataframe["Date"],format="%Y-%m-%d")
dataframe.index=dataframe.Date
dataframe.drop("Date",axis=1,inplace=True)
valued_data=dataframe.values
train=valued_data[:2089,:]
test=valued_data[2089:,:]
scaled_data=Scaler.fit_transform(valued_data)
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
ann=tf.keras.models.Sequential()
# layer 1
ann.add(tf.keras.layers.Dense(units=20,activation="relu"))
# second layer
ann.add(tf.keras.layers.Dense(units=20,activation="relu"))
# third layer
ann.add(tf.keras.layers.Dense(units=1))
ann.compile(optimizer="adam",loss="mean_squared_error",metrics=["accuracy"])
ann.fit(x_train,y_train)

train=dataframe[:2089]
test=dataframe[2089:]
test["Prediction"]=Scaler.inverse_transform(ann.predict(x_test))
plt.figure(1)
plt.title("Model Prediction-ANN")
plt.plot(train["Close"])
plt.plot(test[["Close","Prediction"]])
plt.show()
# prediction_list=[]
# prediction=scaled_data[len(dataframe)-number:,0]
# print(prediction)
# prediction_list.append(prediction)
# main_list=[]
# # print(list(Scaler.inverse_transform(mlr.predict(prediction_list).reshape(-1,1)))[0][0])
# print(list(ann.predict(np.array(prediction_list)))[0][0])
# for i in range(number):
#     prediction_list=[]
#     prediction=list(scaled_data[len(dataframe)-number+i:,0])
#     if main_list==[]:
#         pass
#     else:
#         for i in main_list:
#             prediction.append(i)
#     prediction_list.append(prediction)
#     main_list.append(list(ann.predict(np.array(prediction_list)))[0][0])
# # l=list(Scaler.inverse_transform(np.array(main_list)))
# l=list(Scaler.inverse_transform(np.array(main_list).reshape(-1,1)))
# p=[]
# for i in l:
#     p.append(round(i[0],2))
# Data_frame=pd.DataFrame(index=range(len(p)),columns=["Prediction"])
# for i in range(len(p)):
#     Data_frame["Prediction"][i]=int(p[i])
# plt.figure(2)
# plt.title("Future 30 Days prediction for RELIANCE STOCK-ANN")
# plt.plot(Data_frame["Prediction"])
# plt.figure(3)
# todays_date = datetime.datetime.now().date()
# index = pd.date_range(todays_date, periods=number, freq='D')
# df = pd.DataFrame(index=index, columns=["Prediction"])
# for i in range(len(p)):
#     df["Prediction"][i]=p[i]
# plt.title("Overall Figure-ANN")
# plt.plot(train["Close"],label="Actuall")
# plt.plot(test["Close"],label="Actuall Testing")
# plt.plot(test["Prediction"],label="Test Prediction")
# plt.plot(df["Prediction"],label="Future")
# plt.legend()
# plt.figure(4)
# plt.title("ANN")
# plt.plot(test["Close"],label="Actuall Testing")
# plt.plot(test["Prediction"],label="Test Prediction")
# plt.plot(df["Prediction"],label="Future")
# plt.legend()
# plt.show()
# print(df["Prediction"])