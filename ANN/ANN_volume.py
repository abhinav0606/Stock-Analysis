import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
Scaler=MinMaxScaler(feature_range=(0,1))
import tensorflow as tf
dataset=pd.read_excel("/home/abhinav/PycharmProjects/StockMarket_Prediction/RELIANCE.NS.xlsx")
dataset["Date"]=pd.to_datetime(dataset.Date,format="%Y-%m-%d")
dataset.index=dataset.Date
dataframe=pd.DataFrame(index=range(len(dataset)),columns=["Date","Close"])
for i in range(len(dataset)):
    dataframe["Date"][i]=dataset["Date"][i]
    dataframe["Close"][i]=dataset["Close"][i]
dataframe.index=dataframe.Date
dataframe.drop("Date",axis=1,inplace=True)
values=dataframe.values
scaled_data=Scaler.fit_transform(values)
Train=values[:2221,:]
Test=values[2221:,:]
X_train,Y_train=[],[]
for i in range(60,len(Train)):
    l=list(scaled_data[i-60:i,0])
    l.append(dataset["Volume"][i-1])
    X_train.append(l)
    Y_train.append(scaled_data[i,0])
X_train,Y_train=np.array(X_train),np.array(Y_train)
X_test,Y_test=[],[]
for i in range(len(Train),len(dataset)):
    l=list(scaled_data[i-60:i,0])
    l.append(dataset["Volume"][i-1])
    X_test.append(l)
    Y_test.append(scaled_data[i,0])
X_test,Y_test=np.array(X_test),np.array(Y_test)
# creating ann model
ann=tf.keras.models.Sequential()
# first_layer
ann.add(tf.keras.layers.Dense(units=6,activation="relu"))
# second layer
ann.add(tf.keras.layers.Dense(units=6,activation="relu"))
# third layer
ann.add(tf.keras.layers.Dense(units=1))
ann.compile(optimizer="adam",loss="mean_squared_error",metrics=["accuracy"])
ann.fit(X_train,Y_train,batch_size=32,epochs=100)
Train=dataframe[:2221]
Test=dataframe[2221:]
Test["Prediction"]=Scaler.inverse_transform(ann.predict(X_test))
plt.plot(Train["Close"])
plt.plot(Test[["Close","Prediction"]])
plt.show()
ann.save("ANN_volume.h5")