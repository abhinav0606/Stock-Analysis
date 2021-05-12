from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.signin, name="Login"),
    path("register/", views.signup, name="Register"),
    path("changepass/", views.change_password, name="Password_Change"),
    path('', views.main, name="Main Page"),
    path('search/',views.search,name='Search'),
    path('logout/',views.signoff,name="Logout"),
    path('details/',views.details,name="Details"),
    path('details/<str:name>',views.details_single_wise,name="Single"),
    path('compare/',views.compare_input,name="Compare_input")
]
