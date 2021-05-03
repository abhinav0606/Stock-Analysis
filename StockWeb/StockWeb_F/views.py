from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth import authenticate
import matplotlib.pyplot as plt
import io
import urllib,base64
@login_required(login_url="/login")
def main(request):
    if str(request.user)=="StocksW":
        logout(request)
        return HttpResponseRedirect("/login")
    return HttpResponse("Hello Everyone")
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
                    return HttpResponseRedirect(nt)
                else:
                    return HttpResponse(f"Hello Everyone {request.user}")
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
