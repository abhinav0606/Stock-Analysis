import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import datetime
import tensorflow as tf
Scaler=MinMaxScaler(feature_range=(0,1))
data=pd.read_excel("/home/abhinav/PycharmProjects/StockMarket_Prediction/RELIANCE.NS.xlsx")
data["Date"]=pd.to_datetime(data.Date,format="%Y-%m-%d")
data.index=data.Date
dataframe=pd.DataFrame(index=range(len(data)),columns=["Date","Close"])
for i in range(len(data)):
    dataframe["Date"][i]=data["Date"][i]
    dataframe["Close"][i]=data["Close"][i]
dataframe.index=dataframe.Date
dataframe.drop("Date",axis=1,inplace=True)
values_data=dataframe.values
train=values_data[:2089,:]
test=values_data[2089:,:]
scaled_data=Scaler.fit_transform(values_data)
x_train,y_train=[],[]
for i in range(60,len(train)):
    x_train.append(scaled_data[i-60:i,0])
    y_train.append(scaled_data[i,0])
x_train,y_train=np.array(x_train),np.array(y_train)
x_test,y_test=[],[]
for i in range(len(train),len(dataframe)):
    x_test.append(scaled_data[i-60:i,0])
    y_test.append(scaled_data[i,0])
x_test,y_test=np.array(x_test),np.array(y_test)
ann=tf.keras.models.Sequential()
# 1st layer
ann.add(tf.keras.layers.Dense(units=20,activation="relu"))
# 2nd layer
ann.add(tf.keras.layers.Dense(units=20,activation="relu"))
# 3rd layer
ann.add(tf.keras.layers.Dense(units=1))
ann.compile(optimizer="adam",loss="mean_squared_error",metrics=["accuracy"])
ann.fit(x_train,y_train,batch_size=64,epochs=100)
# prediction
train=dataframe[:2089]
test=dataframe[2089:]
test["Prediction"]=Scaler.inverse_transform(ann.predict(x_test))
plt.figure(1)
plt.title("Model Prediction-ANN")
plt.plot(train["Close"])
plt.plot(test[["Close","Prediction"]])

prediction_list=[]
prediction=scaled_data[len(dataframe)-60:,0]
print(prediction)
prediction_list.append(prediction)
main_list=[]
# print(list(Scaler.inverse_transform(mlr.predict(prediction_list).reshape(-1,1)))[0][0])
print(list(ann.predict(np.array(prediction_list)))[0][0])
for i in range(30):
    prediction_list=[]
    prediction=list(scaled_data[len(dataframe)-60+i:,0])
    if main_list==[]:
        pass
    else:
        for i in main_list:
            prediction.append(i)
    prediction_list.append(prediction)
    main_list.append(list(ann.predict(np.array(prediction_list)))[0][0])
# l=list(Scaler.inverse_transform(np.array(main_list)))
l=list(Scaler.inverse_transform(np.array(main_list).reshape(-1,1)))
p=[]
for i in l:
    p.append(round(i[0],2))
Data_frame=pd.DataFrame(index=range(len(p)),columns=["Prediction"])
for i in range(len(p)):
    Data_frame["Prediction"][i]=int(p[i])
plt.figure(2)
plt.title("Future 30 Days prediction for RELIANCE STOCK-ANN")
plt.plot(Data_frame["Prediction"])
plt.figure(3)
todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date, periods=30, freq='D')
df = pd.DataFrame(index=index, columns=["Prediction"])
for i in range(len(p)):
    df["Prediction"][i]=p[i]
plt.title("Overall Figure-ANN")
plt.plot(train["Close"],label="Actuall")
plt.plot(test["Close"],label="Actuall Testing")
plt.plot(test["Prediction"],label="Test Prediction")
plt.plot(df["Prediction"],label="Future")
plt.legend()
plt.figure(4)
plt.title("ANN")
plt.plot(test["Close"],label="Actuall Testing")
plt.plot(test["Prediction"],label="Test Prediction")
plt.plot(df["Prediction"],label="Future")
plt.legend()
plt.show()
print(df["Prediction"])