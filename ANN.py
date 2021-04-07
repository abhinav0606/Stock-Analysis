import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
Scaler=MinMaxScaler(feature_range=(0,1))
dataset=pd.read_excel("TCS.NS.xlsx")
dataset["Date"]=pd.to_datetime(dataset.Date,format="%Y-%m-%d")
dataset.index=dataset["Date"]
dataset1=pd.DataFrame(index=range(0,len(dataset)),columns=["Date","Close"])
for i in range(len(dataset)):
    dataset1["Date"][i]=dataset["Date"][i]
    dataset1["Close"][i]=dataset["Close"][i]
dataset1.index=dataset1.Date
dataset1.drop("Date",axis=1,inplace=True)
dataset2=dataset1.values
Train=dataset2[:2221,:]
Test=dataset2[2221:,:]
Scaled_dataset=Scaler.fit_transform(dataset2)
X_train,Y_train=[],[]
for i in range(60,len(Train)):
    X_train.append(Scaled_dataset[i-60:i,0])
    Y_train.append(Scaled_dataset[i,0])
X_train,Y_train=np.array(X_train),np.array(X_train)
# creating ANN
ann=tf.keras.models.Sequential()
# 1st layer
ann.add(tf.keras.layers.Dense(units=6,activation="relu"))
# 2nd layer
ann.add(tf.keras.layers.Dense(units=6,activation="relu"))
# 3rd layer
ann.add(tf.keras.layers.Dense(units=1))
ann.compile(optimizer="adam",loss="mean_squared_error",metrics=["accuracy"])
ann.fit(X_train,Y_train,batch_size=64,epochs=100)
# Testing results
X_test=[]
Y_test=[]
for i in range(len(Train),len(dataset1)):
    X_test.append(Scaled_dataset[i-60:i,0])
    Y_test.append(Scaled_dataset[i,0])
X_test=np.array(X_test)
Train=dataset1[:2221]
Test=dataset1[2221:]
Test["Prediction"]=Scaler.inverse_transform(ann.predict(X_test))
rmse=np.sqrt(np.mean(np.power((np.array(Test['Close'])-np.array(Scaler.inverse_transform(ann.predict(X_test)))),2)))
print(rmse)
plt.title("TCS-STOCK ANALYSIS WITH ANN")
plt.plot(Train["Close"])
plt.plot(Test[["Close","Prediction"]])
plt.show()
ann.save("ANN_MODEL.h5")
# from the ann model it is quite clear that putting previous 60 values it is giving us a quite a good result and now we will see the results with
# lstm model and many more things and we will try this method to various regression techniques.
#Now with this model we will try to predict the values for the next month how the graph will go on.
