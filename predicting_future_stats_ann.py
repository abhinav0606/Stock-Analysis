import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
Scaler=MinMaxScaler(feature_range=(0,1))
model=tf.keras.models.load_model("ANN_MODEL.h5")
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
X_test=[]
Y_test=[]
for i in range(len(Train),len(dataset1)):
    X_test.append(Scaled_dataset[i-60:i,0])
    Y_test.append(Scaled_dataset[i,0])
X_test=np.array(X_test)
Train=dataset1[:2221]
Test=dataset1[2221:]
Test["Prediction"]=Scaler.inverse_transform(model.predict(X_test).reshape(-1,1))
rmse=np.sqrt(np.mean(np.power((np.array(Test['Close'])-np.array(Scaler.inverse_transform(model.predict(X_test)))),2)))
print(rmse)
plt.title("TCS-STOCK ANALYSIS WITH ANN")
# plt.plot(Train["Close"])
plt.plot(Test[["Close","Prediction"]])
plt.show()
# predict_new_value=dataset1["Close"][:-31:-1].values
# predict_new_value=np.reshape(predict_new_value,(-1,1))
# predict_new_value=Scaler.transform(predict_new_value)
# values=[]
# for i in predict_new_value:
#     values.append(i[0])
# values=np.array(values)
# values=values.reshape(1,-1)
# print(values.shape)
# print(X_test.shape)
# print(Scaler.inverse_transform(model.predict(values)))
# print(Scaler.inverse_transform(values))
# print(Scaler.inverse_transform(model.predict(X_test)))