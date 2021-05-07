import pandas as pd
def bse_nse(company):
    if ".BO" not in company and ".NS" not in company:
        return "No Analysis"
    else:
        if ".BO" in company:
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
                return "No Recommender"
            else:
                for i in range(start,end):
                    l.append((dataset[dataset.index==list(dt[group])[i]]["Security Id"]).values[0]+".BO")
                return l
        else:
            dataset=pd.read_excel("company1.xlsx")
            updated_name=company.split(".")[0]
            index=dataset[dataset['Symbol']==updated_name]["Sr. No."]
            start=0
            end=0
            if ((index+1).values[0])>len(dataset):
                start=False
            else:
                start=((index+1).values[0])
            if ((index+6).values[0])>len(dataset):
                end=len(dataset)+1
            else:
                end=((index+6).values[0])
            l=[]
            if start==False:
                return "No Recommender"
            else:
                for i in range(start,end):
                    l.append((dataset[dataset["Sr. No."]==i]["Symbol"]).values[0]+".NS")
                return l