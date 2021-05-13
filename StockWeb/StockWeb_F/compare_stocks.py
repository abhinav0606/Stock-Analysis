from pandas_datareader import data as dt
import pandas as pd
import numpy as np
import io
import base64
import urllib
import matplotlib.pyplot as plt
from Security_return import simple_return
from Log_Return import log_return
from montecarlo_forcast_stock_price import monte_forcast
from Beta import beta
from Prediction import prediction
def compare(company1,company2):
    dicty={}
    # company1
    cp1=dt.DataReader(company1,data_source="yahoo",start="2010-1-1")
    sr=simple_return(company1)
    lr=log_return(company1)
    mcarlo=monte_forcast(company1)
    beta_value=beta(company1)
    prd=prediction(company1)
    plt.figure(8)
    plt.clf()
    plt.title(f"Growth Of {company1.split('.')[0]}")
    plt.plot(cp1["Close"])
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    growth_plot_cp1=urllib.parse.quote(string)
    dicty["Growth_Plot_Cp1"]=growth_plot_cp1
    dicty["Simple_return_Cp1"]=round(sr["Overall_Mean"],3)
    dicty["Simple_return_plot_Cp1"]=sr["Plot"]
    dicty["Log_return_Cp1"]=round(lr["Overall_Mean"],3)
    dicty["Log_return_Plot_Cp1"]=lr["Plot"]
    dicty["Var_Cp1"]=mcarlo["Variance_return"]
    dicty["Std_Cp1"]=mcarlo["Std_deviation"]
    dicty["Drift_Cp1"]=mcarlo["Drift"]
    dicty["Norm_Cp1"]=mcarlo["Norm"]
    dicty["Future_Iteration_Cp1"]=mcarlo['plot']
    dicty["Beta_Cp1"]=beta_value['Beta']
    dicty["Cov_mrkt_wrt_stk_Cp1"]=beta_value['Cov Market wrt Stock']
    dicty["Variance_Market_Cp1"]=beta_value["Var Market"]
    dicty["Volatility_Cp1"]=beta_value["Volatility_of_stock"]
    dicty["Future_Pred_Cp1"]=prd["Plot2"]
    # company2
    cp2=dt.DataReader(company2,data_source="yahoo",start="2010-1-1")
    sr=simple_return(company2)
    lr=log_return(company2)
    mcarlo=monte_forcast(company2)
    beta_value=beta(company2)
    prd=prediction(company2)
    plt.figure(8)
    plt.clf()
    plt.title(f"Growth Of {company2.split('.')[0]}")
    plt.plot(cp2["Close"])
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format="png")
    buf.seek(0)
    string=base64.b64encode(buf.read())
    growth_plot_cp2=urllib.parse.quote(string)
    dicty["Growth_Plot_Cp2"]=growth_plot_cp2
    dicty["Simple_return_Cp2"]=round(sr["Overall_Mean"],3)
    dicty["Simple_return_plot_Cp2"]=sr["Plot"]
    dicty["Log_return_Cp2"]=round(lr["Overall_Mean"],3)
    dicty["Log_return_Plot_Cp2"]=lr["Plot"]
    dicty["Var_Cp2"]=mcarlo["Variance_return"]
    dicty["Std_Cp2"]=mcarlo["Std_deviation"]
    dicty["Drift_Cp2"]=mcarlo["Drift"]
    dicty["Norm_Cp2"]=mcarlo["Norm"]
    dicty["Future_Iteration_Cp2"]=mcarlo['plot']
    dicty["Beta_Cp2"]=beta_value['Beta']
    dicty["Cov_mrkt_wrt_stk_Cp2"]=beta_value['Cov Market wrt Stock']
    dicty["Variance_Market_Cp2"]=beta_value["Var Market"]
    dicty["Volatility_Cp2"]=beta_value["Volatility_of_stock"]
    dicty["Future_Pred_Cp2"]=prd["Plot2"]
compare("RELIANCE.NS","TCS.NS")