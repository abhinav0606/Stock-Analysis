import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# taking in account volume and closig price into account
data=pd.read_excel("/home/abhinav/PycharmProjects/StockMarket_Prediction/MRF.NS.xlsx")
X=data.iloc[:,[4,5]].values
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
# plt.show()
# number_of cluster=4
kmeans=KMeans(n_clusters=2,init="k-means++",random_state=42)
predict_means=kmeans.fit_predict(X)
plt.scatter(X[predict_means==0,0],X[predict_means==0,1],c="red",label="c1")
plt.scatter(X[predict_means==1,0],X[predict_means==1,1],c="blue",label="c2")
# plt.scatter(X[predict_means==2,0],X[predict_means==2,1],c="green",label="c3")
# plt.scatter(X[predict_means==3,0],X[predict_means==3,1],c="yellow",label="c4")
plt.show()