from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth import authenticate
from .sendmail import send
from pandas_datareader import data as dt
import matplotlib.pyplot as plt
import io
import urllib,base64
from .Recommendation_Box import bse_nse
from .Security_return import simple_return
from .Log_Return import log_return
from .Beta import beta
from .Prediction import prediction
from .monte_carlo_derivative import montecarlo_derivative
from .montecarlo_forcast_stock_price import monte_forcast
@login_required(login_url="/login")
def main(request):
    if str(request.user)=="StocksW":
        logout(request)
        return HttpResponseRedirect("/login")
    return render(request,"main_page.html")
def signin(request):
    social_login=list(User.objects.all())
    normal_login=list(Register.objects.all())
    social_username=[]
    normal_username=[]
    login_cred={}
    for i in social_login:
        social_username.append(i.username)
    for i in normal_login:
        normal_username.append(i.username)
        login_cred[i.username]=i.password
    nt=""
    if request.GET:
        nt=request.GET.get('next')
    if request.method=="POST":
        username=request.POST.get("usernamel","default")
        password=request.POST.get("passwordl","default")
        if username=="" or password=="":
            return render(request,"login.html",{"message":"Fill up full form please"})
        if username in social_username or username in normal_username:
            if password==login_cred[username]:
                u=authenticate(request,username=username,password=password)
                login(request,u)
                if nt!="":
                    if nt=="/details/":
                        return HttpResponseRedirect("/search/")
                    return HttpResponseRedirect(nt)
                else:
                    return HttpResponseRedirect("/")
            else:
                return render(request,"login.html",{"message":"Incorrect Password"})
        else:
            return render(request,"login.html",{"message":"Username doesnt exists"})
    return render(request,"login.html",{"message":""})

def signup(request):
    social_login=list(User.objects.all())
    normal_login=list(Register.objects.all())
    social_username=[]
    normal_username=[]
    emaily=[]
    social_email=[]
    for i in social_login:
        social_username.append(i.username)
        social_email.append(i.email)
    for i in normal_login:
        normal_username.append(i.username)
        emaily.append(i.email)
    if request.method=="POST":
        Name=request.POST.get("Name","default")
        username=request.POST.get("username","default")
        password=request.POST.get("password","default")
        password_c=request.POST.get("password-c","default")
        phone=request.POST.get("phone","default")
        email=request.POST.get("email","default")
        print(email)
        if Name=="" or username=="" or password=="" or password_c=="" or phone=="" or email=="":
            return render(request,"registration.html",{"message":"Fill out full form Please"})
        else:
            if username in normal_username or username in social_username:
                return render(request,"registration.html",{"message":"Username Exist"})
            elif email in emaily or email in social_email:
                return render(request,"registration.html",{"message":"Email Exist"})
            elif password!=password_c:
                return render(request,"registration.html",{"message":"Password Doesnt Matched"})
            elif len(phone)!=10:
                return render(request,"registration.html",{"message":"Invalid Phone"})
            else:
                Register(name=Name,username=username,email=email,password=password,phone=phone).save()
                U=User.objects.create_user(username,email,password)
                U.first_name=Name
                U.save()
                send(Name,email)
                return HttpResponseRedirect("/login")
    return render(request,"registration.html",{"message":""})

def change_password(request):
    normal_login=list(Register.objects.all())
    normal_username=[]
    for i in normal_login:
        normal_username.append(i.username)
    if request.method=="POST":
        username=request.POST.get("username","default")
        password=request.POST.get("password","default")
        if username in normal_username:
            user=Register.objects.get(username=username)
            user.password=password
            user.save()
            USER=User.objects.get(username=username)
            USER.set_password(password)
            USER.save()
            return render(request,"login.html",{"message":"Password Changed Successfully"})
        else:
            return render(request,"login.html",{"message":"Username Doesnt Exist"})
    return render(request,"forget_pass.html")
def signoff(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/login")
    else:
        return HttpResponseRedirect("/login")
# Details of stock
@login_required(login_url='/login')
def search(request):
    return render(request,"search_page.html",{"message":""})
@login_required(login_url="/login")
def details(request):
    recom=[]
    if request.method=="POST":
        search=request.POST.get("search","default")
        if search=="":
            return render(request,"search_page.html",{"message":"*Fill the code"})
        try:
            data=dt.DataReader(search,data_source="yahoo")
        except:
            return render(request,"search_page.html",{"message":"*We only deal with NSE and BSE stock.Please Enter the correct code"})
        recom=bse_nse(search)
        if type(recom)==str:
            recom=[]
        elif len(recom)!=5:
            recom=[]
        else:
            pass
        today_price=round(data["Close"][-1],3)
        yesterday_price=round(data["Close"][-2],2)
        #simple return
        sr=simple_return(search)
        simple_mean=sr["Overall_Mean"]
        simple_mean_plot=sr["Plot"]
        #log return
        lr=log_return(search)
        log_mean=lr["Overall_Mean"]
        log_mean_plot=lr["Plot"]
        #beta
        bt=beta(search)
        cov_market_wrt_stock=bt['Cov Market wrt Stock']
        variance_market=bt['Var Market']
        beta_stock=bt['Beta']
        volatility_stock=bt['Volatility_of_stock']
        # mlr prediction
        mlr=prediction(search)
        mlr_previous=mlr["Previous"]
        mlr_today=mlr["Today"]
        mlr_plot1=mlr["Plot1"]
        mlr_plot2=mlr["Plot2"]
        mlr_plot3=mlr["Plot3"]
        mlr_plot4=mlr["Plot4"]
        mlr_upcoming=mlr["Upcoming_Pred"]
        #montecarlo derivative
        montecarlo_d=montecarlo_derivative(search)
        d1=montecarlo_d["D1"][search]
        d2=montecarlo_d["D2"][search]
        bsf=montecarlo_d["BSF"][search]
        s=montecarlo_d["S"][search]
        #montecarloforcast
        monte=monte_forcast(search)
        monte_mean=monte["Mean_return"]
        monte_var=monte["Variance_return"]
        monte_drift=monte["Drift"]
        monte_std=monte["Std_deviation"]
        monte_norm=monte["Norm"]
        monte_plot=monte["plot"]
    return render(request,"details.html",{"recom":recom,"search":search,"today":today_price,"yesterday":yesterday_price,"Simple_mean":simple_mean,"Simple_mean_plot":simple_mean_plot,"log_mean":log_mean,"log_mean_plot":log_mean_plot,
                                          'cov_mar_wrt_stk':cov_market_wrt_stock,'var_market':variance_market,"beta":beta_stock,"Stock_volat":volatility_stock,
                                          "mlr_upcoming":mlr_upcoming,"mlr_today":mlr_today,"mlr_previous":mlr_previous,"plot1":mlr_plot1,"plot2":mlr_plot2,"plot3":mlr_plot3,"plot4":mlr_plot4,
                                          "D1":d1,"D2":d2,"BSF":bsf,"S":s,
                                          "monte_mean":monte_mean,"monte_var":monte_var,"monte_drift":monte_drift,
                                          "monte_std":monte_std,"monte_norm":monte_norm,"monte_plot":monte_plot
                                          })
@login_required(login_url='/login')
def details_single_wise(request,name):
    recom=[]
    search=name
    if search=="":
        return render(request,"search_page.html",{"message":"*Fill the code"})
    try:
        data=dt.DataReader(search,data_source="yahoo")
    except:
        return render(request,"search_page.html",{"message":"*We only deal with NSE and BSE stock.Please Enter the correct code"})
    recom=bse_nse(search)
    if type(recom)==str:
        recom=[]
    elif len(recom)!=5:
        recom=[]
    else:
        pass
    today_price=round(data["Close"][-1],3)
    yesterday_price=round(data["Close"][-2],2)
    #simple return
    sr=simple_return(search)
    simple_mean=sr["Overall_Mean"]
    simple_mean_plot=sr["Plot"]
    #log return
    lr=log_return(search)
    log_mean=lr["Overall_Mean"]
    log_mean_plot=lr["Plot"]
    #beta
    bt=beta(search)
    cov_market_wrt_stock=bt['Cov Market wrt Stock']
    variance_market=bt['Var Market']
    beta_stock=bt['Beta']
    volatility_stock=bt['Volatility_of_stock']
    # mlr prediction
    mlr=prediction(search)
    mlr_previous=mlr["Previous"]
    mlr_today=mlr["Today"]
    mlr_plot1=mlr["Plot1"]
    mlr_plot2=mlr["Plot2"]
    mlr_plot3=mlr["Plot3"]
    mlr_plot4=mlr["Plot4"]
    mlr_upcoming=mlr["Upcoming_Pred"]
    #montecarlo derivative
    montecarlo_d=montecarlo_derivative(search)
    d1=montecarlo_d["D1"][search]
    d2=montecarlo_d["D2"][search]
    bsf=montecarlo_d["BSF"][search]
    s=montecarlo_d["S"][search]
    #montecarloforcast
    monte=monte_forcast(search)
    monte_mean=monte["Mean_return"]
    monte_var=monte["Variance_return"]
    monte_drift=monte["Drift"]
    monte_std=monte["Std_deviation"]
    monte_norm=monte["Norm"]
    monte_plot=monte["plot"]
    return render(request,"single_file.html",{"recom":recom,"search":search,"today":today_price,"yesterday":yesterday_price,"Simple_mean":simple_mean,"Simple_mean_plot":simple_mean_plot,"log_mean":log_mean,"log_mean_plot":log_mean_plot,
                                          'cov_mar_wrt_stk':cov_market_wrt_stock,'var_market':variance_market,"beta":beta_stock,"Stock_volat":volatility_stock,
                                          "mlr_upcoming":mlr_upcoming,"mlr_today":mlr_today,"mlr_previous":mlr_previous,"plot1":mlr_plot1,"plot2":mlr_plot2,"plot3":mlr_plot3,"plot4":mlr_plot4,
                                          "D1":d1,"D2":d2,"BSF":bsf,"S":s,
                                          "monte_mean":monte_mean,"monte_var":monte_var,"monte_drift":monte_drift,
                                          "monte_std":monte_std,"monte_norm":monte_norm,"monte_plot":monte_plot
                                          })
@login_required(login_url="/login")
def compare_input(request):
    if request.method=="POST":
        print(request.POST.get("search1","default"))
        print(request.POST.get("search2", "default"))
    return render(request,"compare.html")