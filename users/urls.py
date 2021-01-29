from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    
    path('login',views.loginPage,name="login_page"),
    path('logout',views.logout,name="logout")
 
]
