# Data Generation for 2 Companies Reliance pvt ltd and TCS.NS(Tata Consultancy Servises)
import pandas as pd
from pandas_datareader import data as dt
import numpy as np
Company_NSE=input("Enter the NSE Code of the Company")
Stock_Data=dt.DataReader(Company_NSE,data_source="yahoo",start="1995-1-1")
Stock_Data["Simple Return"]=(Stock_Data["Adj Close"]/Stock_Data['Adj Close'].shift(1))-1
Stock_Data["Log Return"]=np.log(Stock_Data["Adj Close"]/Stock_Data["Adj Close"].shift(1))
Stock_Data["Normal_100"]=(Stock_Data["Adj Close"]/Stock_Data["Adj Close"].iloc[0])
Stock_Data["Mean"]=Stock_Data["Simple Return"].mean()
Stock_Data["Annual return"]=str(Stock_Data["Simple Return"].mean()*250*100)+"%"
Future_days=50
DF=pd.DataFrame(Stock_Data)
List=[]
for i in range(len(DF)):
    L=[]
    try:
        for j in range(i+1,i+Future_days+1):
            try:
                L.append(DF["Close"][j])
            except:
                L=[]
    except:
        pass
    if len(L)==0:
        List.append(np.NaN)
    else:
        List.append((sum(L)/len(L)))

DF["Prediction"]=List
DF.to_excel(Company_NSE+".xlsx")
