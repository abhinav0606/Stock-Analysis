import pandas as pd
name=input("Enter the Company Name")
dataset=pd.read_excel("company.xlsx")
updated_name=name[:-3]
index=dataset[dataset['Symbol']==updated_name]["Sr. No."]
start=((index+1).values)[0]
end=((index+6).values)[0]
l=[]
for i in range(start,end):
    l.append((dataset[dataset["Sr. No."]==i]["Symbol"]).values[0])
print(l)