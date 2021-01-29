from django.shortcuts import render,redirect
from store.models import *
from store.views import store
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import auth
import json

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("/store")
            
    errors=None
    
    if request.method=="POST":
        data=request.POST
        
        if "login_form" in data:
            print("login submitted")
            errors= handleLogin(request,data)
            
        elif "register_form" in data:
            print("register submitted")
            errors = handleRegister(request,data)
            print("errors:",errors)
            print(data)
        
        if len(errors) == 0:
            
            return redirect("/store")
        else:
            print("errors",errors)
            return render(request,"login.html",{"errors" : errors})
            
             
    else:   
        return render(request,"login.html",{"errors" : errors})
    
    
def handleLogin(request,data):
    
    errors=[]
    if User.objects.filter(email=data["email"]).exists():
        login_user=User.objects.get(email=data["email"])
        
        if auth.authenticate(username=login_user.username,password=data["pass"]) is not None :
            auth.login(request,login_user)
        else:
            errors.append("The entered password is incorrect")
            
    else:
        errors.append("We cannot find an account with that email address")
        
    return errors
    

        

def handleRegister(request,data):
    errors=[]
    valid=True
    input_user=data["username"]
    input_pass=data["pass"]
    input_confirm=data["confirm_pass"]
    input_email=data["email"]
    
    if User.objects.filter(email=input_email).exists():
        print("email taken")
        errors.append("Email already taken")
        valid=False
        
    if User.objects.filter(username=input_user).exists():
        errors.append("User name already taken")
        valid=False
    
    if input_pass != input_confirm:
        print("passwords dont match")
        errors.append("Passwords dont match")
        valid=False
        
    if valid:
        print("created user")
        new_user=User(username=input_user,email=input_email)
        new_user.set_password(input_pass)
        new_customer=Customer(name=input_user,email=input_email,user=new_user)
        new_user.save()
        new_customer.save()
        auth.login(request,new_user)
        
        
    return errors
 
    
def logout(request):
    if json.loads(request.body):
        
        json_data=json.loads(request.body)
        
        if json_data["logout"]:
            auth.logout(request)
            return  JsonResponse('logged out', safe=False)
    else:
        print("no logout")
        return JsonResponse('No logout', safe=False)
   
        
      
        
        
    
    
        
        
        
    
   
    
    
