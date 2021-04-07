import pandas as pd
import numpy as np
import warnings
Company=input("Enter the NSE code of the company")
data=pd.read_excel(Company+".xlsx")
new_df=pd.DataFrame(index=range(len(data)),columns=["Date","Close"])
for i in range(len(data)):
    new_df["Date"][i]=data["Date"][i]
    new_df["Close"][i]=data["Close"][i]
Train=new_df[:982]
Test=new_df[982:]
# print(Train.shape)
# /print(Test.shape)
prediction=[]
for i in range(0,Test.shape[0]):
    a=Train["Close"][len(Train)-314+i:].sum()+sum(prediction)
    b=a/314
    prediction.append(b)
# print(len(prediction))
rms=np.sqrt(np.mean(np.power((np.array(Test['Close'])-prediction),2)))
import matplotlib.pyplot as plt
Test["Prediction"]=prediction
plt.figure(1)
plt.title(f"Moving Average-------Past Data   {rms}")
plt.plot(Train["Close"])
plt.plot(Test[["Close","Prediction"]])
warnings.filterwarnings("ignore")
# print(Test["Close"])
# print(Test["Prediction"])
X_train=pd.to_numeric(pd.to_datetime(Train["Date"],format='%Y-%m-%d'))
X_test=pd.to_numeric(pd.to_datetime(Test["Date"],format='%Y-%m-%d'))
Y_train=Train["Close"].values
Y_test=Test["Close"].values
X_train=np.array(X_train).reshape(-1,1)
Y_train=Y_train.reshape(-1,1)
X_test=np.array(X_test).reshape(-1,1)
Y_test=Y_test.reshape(-1,1)
from sklearn.linear_model import LinearRegression
Lr=LinearRegression()
Lr.fit(X_train,Y_train)
Test["Linear_R"]=Lr.predict(X_test)
rmse=np.sqrt(np.mean(np.power((np.array(Test['Close'])-np.array(Lr.predict(X_test))),2)))
plt.figure(2)
plt.title(f"Linear Regression-------Past Data   {rmse}")
plt.plot(Train["Close"])
plt.plot(Test[["Close","Linear_R"]])
plt.show()



# From this above program it is clear that based on the average of the past data
# and applying linear regression the plots are not that much accurate
