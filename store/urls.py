from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    
    path('',views.store,name="home"),
    path('cart/',views.cart,name="cart"),
    path('store/',views.store,name="store"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_cart/',views.updateCart,name="update_cart"),
    path('process_order/',views.processOrder,name="process_order"),
    path('clear_cart/',views.clearCart,name="clear_cart"),
    path('product/<slug:product_name>/<int:product_id>/',views.productDetails,name="product_details"),
    path('search',views.search,name="search")
    
]
