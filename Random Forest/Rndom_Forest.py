import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
Scaler=MinMaxScaler(feature_range=(0,1))
dataset=pd.read_excel("TCS.NS.xlsx")
dataset["Date"]=pd.to_datetime(dataset["Date"],format="%Y-%m-%d")
dataset.index=dataset.Date
dataframe=pd.DataFrame(index=range(len(dataset)),columns=["Date","Close"])
for i in range(len(dataset)):
    dataframe["Date"][i]=dataset["Date"][i]
    dataframe["Close"][i]=dataset["Close"][i]
dataframe.index=dataframe.Date
dataframe.drop("Date",axis=1,inplace=True)
values=dataframe.values
scaled_dataset=Scaler.fit_transform(values)
Train_data=values[:2221,:]
Test_data=values[2221:,:]
X_train,X_test,Y_train,Y_test=[],[],[],[]
for i in range(60,len(Train_data)):
    X_train.append(scaled_dataset[i-60:i,0])
    Y_train.append(scaled_dataset[i,0])
for i in range(len(Train_data),len(dataframe)):
    X_test.append(scaled_dataset[i-60:i,0])
    Y_test.append(scaled_dataset[i,0])
X_train,Y_train,X_test,Y_test=np.array(X_train),np.array(Y_train),np.array(X_test),np.array(Y_test)
rdnf=RandomForestRegressor(n_estimators=20,random_state=0)
rdnf.fit(X_train,Y_train)
Train_data=dataframe[:2221]
Test_data=dataframe[2221:]
Test_data["Prediction"]=Scaler.inverse_transform(rdnf.predict(X_test).reshape(-1,1))
plt.figure(1)
plt.plot(Train_data["Close"])
plt.plot(Test_data[["Close","Prediction"]])
plt.figure(2)
plt.scatter(Test_data.index[:-350:-1],Test_data["Close"][:-350:-1])
plt.plot(Test_data["Prediction"][:-350:-1])
plt.show()