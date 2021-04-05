import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
company=input("Enter the company name")
file_name=company+".xlsx"
data=pd.read_excel(file_name)
sb.set()
plt.plot(data["Close"][:-7])
plt.plot(data["Prediction"][:-7])
plt.show()
