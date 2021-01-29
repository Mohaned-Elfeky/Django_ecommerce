from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer (models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
    

    @property
    def imageUrl(self):
        try:
            url=self.image.url
        except :
            url=""
        return url


class Order(models.Model):
    Customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)


    

    @property
    def get_order_total(self):
        items=self.orderitem_set.all()
        total=0
        for item in  items:
            total+=item.Product.price*item.quantity
        return total

    @property
    def get_order_quantity(self):
        items=self.orderitem_set.all()
        total=0
        for item in  items:
            total+=item.quantity
        return total

    @property
    def is_shipping(self):
        shipping=False
        order_items=OrderItem.objects.filter(Order=self)
        for item in order_items:
            if item.Product.digital==False:
                shipping=True
        return shipping

    @property
    def get_first_img(self):
        order_items=OrderItem.objects.filter(Order=self)
        if len(order_items)>0:
         return order_items[0].Product.imageUrl
        else:
            return ""

    
    # @classmethod
    # def empty_order(cls):
    #     empty_order=cls(Customer=None)
    #     return empty_order


    

class OrderItem(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    Order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=1,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        return self.Product.price * self.quantity

class ShippingAddress(models.Model):
    Customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    Order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

   

    


