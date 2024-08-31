from django.db import models
from django.contrib.auth.models import User

data = {
    ("Groccery","Groccery"),
    ("Fruit","Fruit"),
    ("Vegitables","Vegitbales"),
    ("Electronics","Electronics")
}

class Login(models.Model):
    username = models.CharField(max_length=400,blank=False)
    password = models.CharField(max_length=500,blank=False)

    def __str__(self):
        return self.username
    
class Product(models.Model):
    item = models.CharField(max_length=400,blank=False)
    des = models.TextField(max_length=600,blank=False)
    price = models.TextField(max_length=600,blank=False)
    sales_price = models.TextField(max_length=600,blank=False)
    stock = models.CharField(max_length=400,blank=False)
    img = models.ImageField(upload_to='images/', blank=True)
    cate=models.CharField(choices=data, blank=True, max_length=20)

    def __str__(self):
        return self.item
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.quantity} x {self.product.item}'