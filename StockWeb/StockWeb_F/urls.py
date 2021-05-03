from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.signin, name="Login"),
    path("register/", views.signup, name="Register"),
    path("changepass/", views.change_password, name="Password_Change"),
    path('', views.main, name="Main Page"),
]
