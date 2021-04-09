import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
Scaler=MinMaxScaler(feature_range=(0,1))
main_data=pd.read_excel("TCS.NS.xlsx")
main_data["Date"]=pd.to_datetime(main_data["Date"],format="%Y-%m-%d")
main_data.index=main_data.Date
data_frame=pd.DataFrame(index=range(len(main_data)),columns=["Date","Close"])
for i in range(len(main_data)):
    data_frame["Date"][i]=main_data["Date"][i]
    data_frame["Close"][i]=main_data["Close"][i]
data_frame.index=data_frame.Date
data_frame.drop("Date",axis=1,inplace=True)
values_dataset=data_frame.values
scaled_dataset=Scaler.fit_transform(values_dataset)
Train=values_dataset[:2221,:]
Test=values_dataset[2221:,:]
X_train,Y_train=[],[]
for i in range(60,len(Train)):
    X_train.append(scaled_dataset[i-60:i,0])
    Y_train.append(scaled_dataset[i,0])
X_test,Y_test=[],[]
for i in range(len(Train),len(data_frame)):
    X_test.append(scaled_dataset[i-60:i,0])
    Y_test.append(scaled_dataset[i,0])
X_train,Y_train,X_test,Y_test=np.array(X_train),np.array(Y_train),np.array(X_test),np.array(Y_test)
from sklearn.tree import DecisionTreeRegressor
dt=DecisionTreeRegressor(random_state=5)
dt.fit(X_train,Y_train)
Train=data_frame[:2221]
Test=data_frame[2221:]
Test["Prediction"]=Scaler.inverse_transform(dt.predict(X_test).reshape(-1,1))
# plt.plot(Train["Close"])
plt.figure(1)
plt.title("ANALYSIS WITH DECISION TREE")
plt.plot(Test[["Close","Prediction"]])
plt.legend(["REAL","PREDICTION"])
plt.figure(2)
plt.title("ANALYSIS WITH DECISION TREE PREVIOUS 50 VALUES")
plt.scatter(Test.index[:-50:-1],Test["Close"][:-50:-1])
plt.plot(Test["Prediction"][:-50:-1])
plt.show()