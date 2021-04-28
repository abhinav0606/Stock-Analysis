import pandas as pd
company=input("Enter the Company name")
upated_name=company.split(".")[0]
dataset=pd.read_csv("Equity.csv")
dt=dataset.groupby("Group").groups
group=(dataset[dataset['Security Id']==upated_name]["Group"]).values[0]
indexy=(dataset[dataset['Security Id']==upated_name].index).values[0]
l=[]
start=list(dt[group]).index(indexy)+1
end=list(dt[group]).index(indexy)+6
if start>=len(list(dt[group])):
    start=False
else:
    start=list(dt[group]).index(indexy)+1
if end>=len(list(dt[group])):
    end=len(list(dt[group]))
else:
    end=list(dt[group]).index(indexy)+6
if start==False:
    print("No Recommender")
else:
    for i in range(start,end):
        l.append((dataset[dataset.index==list(dt[group])[i]]["Security Id"]).values[0])
    print(l)