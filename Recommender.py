import pandas as pd
name=input("Enter the Company Name")
dataset=pd.read_excel("company1.xlsx")
updated_name=name.split(".")[0]
index=dataset[dataset['Symbol']==updated_name]["Sr. No."]
start=0
end=0
print(dataset[dataset["Sr. No."]==1920])
if ((index+1).values[0])>len(dataset):
    start=False
else:
    start=((index+1).values[0])
if ((index+6).values[0])>len(dataset):
    end=len(dataset)+1
else:
    end=((index+6).values[0])
l=[]
print(start)
print(end)
if start==False:
    print("No Recommender")
else:
    for i in range(start,end):
        l.append((dataset[dataset["Sr. No."]==i]["Symbol"]).values[0])
    print(l)