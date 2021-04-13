import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
Scaler=MinMaxScaler(feature_range=(0,1))
dataset=pd.read_excel("/home/abhinav/PycharmProjects/StockMarket_Prediction/RELIANCE.NS.xlsx")
dataset["Date"]=pd.to_datetime(dataset.Date,format="%Y-%m-%d")
dataset.index=dataset.Date
dataframe=pd.DataFrame(index=range(len(dataset)),columns=["Date","Close"])
for i in range(len(dataset)):
    dataframe["Date"][i]=dataset["Date"][i]
    dataframe["Close"][i]=dataset["Close"][i]
dataframe.index=dataframe.Date
dataframe.drop("Date",axis=1,inplace=True)
valued_data=dataframe.values
train=valued_data[:2221,:]
test=valued_data[2221:,:]
scaled_data=Scaler.fit_transform(valued_data)
x_train,y_train=[],[]
for i in range(60,len(train)):
    l=list(scaled_data[i-60:i,0])
    l.append(dataset["Volume"][i])
    x_train.append(l)
    y_train.append(scaled_data[i,0])
x_train,y_train=np.array(x_train),np.array(y_train)
x_test,y_test=[],[]
for i in range(len(train),len(dataset)):
    l=list(scaled_data[i-60:i,0])
    l.append(dataset["Volume"][i])
    x_test.append(l)
    y_test.append(scaled_data[i,0])
x_test,y_test=np.array(x_test),np.array(y_test)
from sklearn.tree import DecisionTreeRegressor
dtr=DecisionTreeRegressor(random_state=0)
dtr.fit(x_train,y_train)
train=dataframe[:2221]
test=dataframe[2221:]
test["Prediction"]=Scaler.inverse_transform(dtr.predict(x_test).reshape(-1,1))
plt.figure(1)
plt.plot(train["Close"])
plt.plot(test[["Close","Prediction"]])
plt.show()