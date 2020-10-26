from django.db import models
from Physical.models import Products, Detail
# Create your models here
# 
# 
# 
class CartItem(models.Model):
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart',on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, blank=True ,on_delete= models.CASCADE)
    imei = models.ForeignKey(Detail, null=True, blank=True, on_delete= models.CASCADE)
    price = models.FloatField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    def __str__(self):
        return str(self.cart.id)
class Cart(models.Model):

    #items = models.ManyToManyField(CartItem, null=True, blank=True)
    #products = models.ManyToManyField(Products, null=True, blank=True)
    totals = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return "Cart id: %s" %(self.id)