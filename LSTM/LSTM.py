import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
Scaler=MinMaxScaler(feature_range=(0,1))
dataset=pd.read_excel("/home/abhinav/PycharmProjects/StockMarket_Prediction/RELIANCE.NS.xlsx")
dataset["Date"]=pd.to_datetime(dataset.Date,format="%Y-%m-%d")
dataframe=pd.DataFrame(index=range(len(dataset)),columns=["Date","Close"])
for i in range(len(dataset)):
    dataframe["Date"][i]=dataset["Date"][i]
    dataframe["Close"][i]=dataset["Close"][i]
dataframe.index=dataframe.Date
dataframe.drop("Date",axis=1,inplace=True)
values=dataframe.values
train=values[:2221,:]
test=values[2221:,:]
scaled_data=Scaler.fit_transform(values)
x_train,y_train=[],[]
for i in range(60,len(train)):
    x_train.append(scaled_data[i-60:i,0])
    y_train.append(scaled_data[i,0])
x_train,y_train=np.array(x_train),np.array(y_train)
x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))
x_test,y_test=[],[]
for i in range(len(train),len(dataframe)):
    x_test.append(scaled_data[i-60:i,0])
    y_test.append(scaled_data[i,0])
x_test,y_test=np.array(x_test),np.array(y_test)
x_test=np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
# creating lstm layer
lstm=tf.keras.models.Sequential()
# adding 1st layers
lstm.add(tf.keras.layers.LSTM(units=50,activation="relu",return_sequences=True,input_shape=(x_train.shape[1],1)))
# lstm.add(tf.keras.layers.Dropout(0.2))
# adding 2nd layers
# lstm.add(tf.keras.layers.LSTM(units=50,return_sequences=True))
# lstm.add(tf.keras.layers.Dropout(0.2))
# adding 3rd layers
# lstm.add(tf.keras.layers.LSTM(units=50,return_sequences=True))
# lstm.add(tf.keras.layers.Dropout(0.2))
# adding 4th layer
lstm.add(tf.keras.layers.LSTM(units=50,activation="relu"))
# lstm.add(tf.keras.layers.Dropout(0.2))
# adding 5th layer
lstm.add(tf.keras.layers.Dense(units=1))
# compiling
lstm.compile(optimizer="adam",loss="mean_squared_error",metrics=["accuracy"])
lstm.fit(x_train,y_train,batch_size=1,epochs=1,verbose=2)
test=dataframe[2221:]
train=dataframe[:2221]
test["Prediction"]=Scaler.inverse_transform(lstm.predict(x_test))
plt.plot(train["Close"])
plt.plot(test[["Close","Prediction"]])
plt.show()
lstm.save("lstm.h5")