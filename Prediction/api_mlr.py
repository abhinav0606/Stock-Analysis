import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as dt
from sklearn.preprocessing import MinMaxScaler
import datetime
Scaler=MinMaxScaler(feature_range=(0,1))
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
from sklearn.linear_model import LinearRegression
mlr=LinearRegression()
mlr.fit(x_train,y_train)
train=dataframe[:2089]
test=dataframe[2089:]
test["Prediction"]=Scaler.inverse_transform(mlr.predict(x_test).reshape(-1,1))
plt.figure(1)
plt.plot(train["Close"],label="Training")
plt.plot(test["Close"],label="Testing")
plt.plot(test["Prediction"],label="Prediction")
plt.legend()
# future_prediction
prediction_list=[]
prediction=scaled_data[len(dataframe)-(number+1):len(dataframe)-1,0]
prediction_list.append(prediction)
print(Scaler.inverse_transform(mlr.predict(prediction_list).reshape(-1,1)))
prediction_list=[]
prediction=scaled_data[len(dataframe)-(number):len(dataframe),0]
prediction_list.append(prediction)
print(Scaler.inverse_transform(mlr.predict(prediction_list).reshape(-1,1)))
main_list=[]
for i in range(number):
    prediction_list=[]
    prediction=list(scaled_data[len(dataframe)-number+i:,0])
    if main_list==[]:
        pass
    else:
        for i in main_list:
            prediction.append(i)
    prediction_list.append(prediction)
    main_list.append(mlr.predict(prediction_list))
l=list(Scaler.inverse_transform(main_list))
p=[]
for i in l:
    p.append(round(i[0],2))
Data_frame=pd.DataFrame(index=range(len(p)),columns=["Prediction"])
for i in range(len(p)):
    Data_frame["Prediction"][i]=int(p[i])
plt.figure(2)
plt.title("Future 30 Days prediction for RELIANCE Stock-MLR")
plt.plot(Data_frame["Prediction"])
plt.figure(3)
todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date, periods=number, freq='D')
df = pd.DataFrame(index=index, columns=["Prediction"])
for i in range(len(p)):
    df["Prediction"][i]=p[i]
plt.title("Overall Figure-MLR")
plt.plot(train["Close"],label="Actuall")
plt.plot(test["Close"],label="Actuall Testing")
plt.plot(test["Prediction"],label="Test Prediction")
plt.plot(df["Prediction"],label="Future")
plt.legend()
plt.figure(4)
plt.title("MLR")
plt.plot(test["Close"],label="Actuall Testing")
plt.plot(test["Prediction"],label="Test Prediction")
plt.plot(df["Prediction"],label="Future")
plt.legend()
# plt.show()
print(df["Prediction"])