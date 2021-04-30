from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .model import Register
from django.contrib.auth import authenticate
import matplotlib.pyplot as plt
import io
import urllib,base64
def signin(request):
    return render(request,"login.html")

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
            return HttpResponseRedirect("/login")
    return render(request,"forget_pass.html")
