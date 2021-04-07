# THIS MODEL IS FOR GIVING THE PREDICTION OF AVERAGE STOCK VALUE FOR THE 30 DAYS
# LIKE ANALYZING THE PREVIOUS DATA AND GETTING THE AVERAGE FOR 15 DAYS SO THIS MODEL IS GIVING US THE
# ACCURACY OF 92 %.........SO IF SOMEONE BOUGHT A STOCK TODAY SO ON AN AVERAGE HE CAN SEE
# HOW MUCH HIS STOCK IS GONNA PERFORM FOR A MONTH ON AN AVERAGE BASED ON PREVIOUS
# VALUES.........................
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sb
from Dataset_generation import future
sb.set()
# data preprocessing
company=input("Enter the company")
data=pd.read_excel(company+".xlsx")
X=data["Close"][:-future()].values
Y=data["Prediction"][:-future()].values
print()
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)
X_train=X_train.reshape(-1,1)
Y_train=Y_train.reshape(-1,1)
X_test=X_test.reshape(-1,1)
Y_test=Y_test.reshape(-1,1)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
Lr=LinearRegression()
Lr.fit(X_train,Y_train)
testing=data["Close"].values.reshape(-1,1)
predicted_values=Lr.predict(sc.transform(testing))
d={}
length=0
for i in predicted_values:
    d[length]=i[0]
    length=length+1
plt.title("TCS-STOCK ANALYSIS")
plt.plot(data["Close"])
plt.plot(list(d.keys()),list(d.values()))
plt.show()
print(Lr.predict(sc.transform([[3050]])))
from sklearn.metrics import r2_score
print(r2_score(Y_test,Lr.predict(X_test)))