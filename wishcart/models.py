from django.db import models
from django.contrib.auth.models import User

from products.models import Color, Product, Size
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True,null=True,blank=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()
    vendor = models.CharField(max_length=15,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    vendor = models.CharField(max_length=15,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"