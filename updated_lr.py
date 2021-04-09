import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
Scaler=MinMaxScaler(feature_range=(0,1))
dataset=pd.read_excel("RELIANCE.NS.xlsx")
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
X_train,Y_train=np.array(X_train),np.array(Y_train)
X_test=[]
Y_test=[]
for i in range(len(Train),len(dataset1)):
    X_test.append(Scaled_dataset[i-60:i,0])
    Y_test.append(Scaled_dataset[i,0])
X_test=np.array(X_test)
Train=dataset1[:2221]
Test=dataset1[2221:]
from sklearn.linear_model import LinearRegression,LogisticRegression
LR=LinearRegression()
LR.fit(X_train,Y_train)
Test["Prediction"]=Scaler.inverse_transform(LR.predict(X_test).reshape(-1,1))
# plt.plot(Train["Close"])

plt.title("Linear Regression-->Analysis of Stock--Input=(Previous 60 values)")
# plt.plot(Test[["Close","Prediction"]])
plt.scatter(Test.index[:-100:-1],Test["Close"][:-100:-1],label="Real Values")
plt.plot(Test["Prediction"][:-100:-1],label="Prediction")
# plt.legend(["Predicted Value"])
plt.show()