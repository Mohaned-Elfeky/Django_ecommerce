from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def get_order(request):
    if request.user.is_authenticated:
        curr_customer=request.user.customer
        order, created=Order.objects.get_or_create(Customer=curr_customer,complete=False)
        items=OrderItem.objects.filter(Order=order)
        quantity=0
        for item in items:
            quantity += item.quantity

        # items=order.orderitem_set.all()    both work
        # print(type(items))
    else:
        order=Order(Customer=None)
        items=[]
        quantity=0

    
    return order,items,quantity
    
def get_username(request):
    if request.user.is_authenticated:
        username=request.user.username
    else:
        username="Guest"
    return username

# Create your views here.

def home(request):

    order,items,quantity=get_order(request)
  

    return render(request,'home.html',{"quantity":quantity,"username":request.user.username})



@login_required(login_url='/login')
def cart(request):
    
    order,items,quantity=get_order(request)
    
    context={

    'items':items,
    'order':order,
    'quantity':quantity,
    "username":get_username(request),
    "logged_in":request.user.is_authenticated
    }

    return render(request,'cart.html',context)

def store(request):
   order,items,quantity=get_order(request)
   products=Product.objects.all()
   context={
       'products':products,
       'quantity':quantity,
       "username":get_username(request),
       "logged_in":request.user.is_authenticated
         }
    
   name=request.user
   print("name= ",name)
      
   return render(request,"store.html",context)
    

@login_required(login_url='/login')
def checkout(request):

    order,items,quantity=get_order(request)
    finished_orders=Order.objects.filter(Customer=request.user.customer,complete=True)
    print(len(finished_orders))
   

    context={

    'items':items,
    'order':order,
    'quantity':quantity,
    'complete_orders':finished_orders,
    "username":get_username(request),
    "logged_in":request.user.is_authenticated
    
    }

    return render(request,'checkout.html',context)
  

def productDetails(request,product_name,product_id):
    order,items,quantity=get_order(request)
    product=Product.objects.get(id=product_id)
    context={
        "username":get_username(request),
        "logged_in":request.user.is_authenticated,
        "product":product,
        "quantity":quantity
        
    }
    
    return render(request,"product_details.html",context)  

def search(request):
    order,items,quantity=get_order(request)
    if request.method == "GET":
        print("in search")
        results=[]
        
        search_key=request.GET["key"]
        products=Product.objects.all()
        for product in products:
            if search_key.lower() in product.name.lower():
                results.append(product)
                
    
    context={
        "username":get_username(request),
        "quantity":quantity,
        "logged_in":request.user.is_authenticated,
        "search_key":search_key,
        "results":results,
        "numberof_results":len(results)
        }
        
        
    return render(request,"search.html",context)

def updateCart(request):
    # if not request.user.is_authenticated:
    #     print("login first")
    data=json.loads(request.body)
    product_id=data['product_id']
    action=data['action']
    curr_product=Product.objects.get(id=product_id)
    curr_order,items,quantity=get_order(request)
    curr_item, created=OrderItem.objects.get_or_create(Order=curr_order,Product=curr_product)
  
    if created:
        curr_item.quantity=1

    elif action=="add":
        curr_item.quantity+=1

    if action=="remove":
        curr_item.quantity-=1

    curr_item.save()

    if curr_item.quantity <= 0:
        curr_item.delete()

    return JsonResponse('Item was added', safe=False)
    



def processOrder(request):
     
     curr_order,items,quantity=get_order(request)
     transaction_key=hash(f"{request.user.customer.name} {curr_order.get_order_total}")
     print(transaction_key)
     curr_order.transaction_id=transaction_key
     curr_order.complete=True
     curr_order.save()
     
     return JsonResponse("lol" , safe=False)



def clearCart(request):
     curr_order,items,quantity=get_order(request)
     print(len(items))
     for item in items:
         item.delete()
     
     return JsonResponse("lol" , safe=False)









