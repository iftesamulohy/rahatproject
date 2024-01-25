from django.db import models
from django.contrib.auth.models import User
from coupon.models import Cuopone

from products.models import Color, Product, Size
# Create your models here.
class OrderedProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    vendor = models.CharField(max_length=15,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    ordered_product = models.ManyToManyField(OrderedProduct)
    amount = models.FloatField()
    OPTIONa = 'Hold'
    OPTIONb = 'Shipment'
    OPTIONc = 'Delivered'
    OPTIONd = 'Canceled'
    CHOICES3 = (
        (OPTIONa, 'Hold'),
        (OPTIONb, 'Shipment'),
        (OPTIONc, 'Delivered'), 
        (OPTIONd, 'Canceled'), 
        
    )

    OPTIONe = 'Cash on Delivery'
    OPTIONf = 'Bkash'
    OPTIONg = 'Rocket'
    OPTIONh = 'Nagad'
    CHOICES4 = (
        (OPTIONe, 'Cash on Delivery'),
        (OPTIONf, 'Bkash'),
        (OPTIONg, 'Rocket'), 
        (OPTIONh, 'Nagad'), 
        
    )
    
    OPTIONi = 'Pending'
    OPTIONj = 'Successful'
    OPTIONk = 'Canceled'
    CHOICES5 = (
        
        (OPTIONi, 'Pending'),
        (OPTIONj, 'Successful'), 
        (OPTIONk, 'Canceled'), 
        
    )
    order_status = models.CharField(max_length=50, choices=CHOICES3,blank=True,null=True)
    payment_method = models.CharField(max_length=50, choices=CHOICES4,blank=True,null=True)
    payment_number = models.CharField(max_length=20,blank=True,null=True)
    transaction_id = models.CharField(max_length=20,blank=True,null=True)
    payment_status = models.CharField(max_length=50, choices=CHOICES5,blank=True,null=True)
    date = models.DateField(null=True,blank=True)
    used_cuopone = models.ManyToManyField(Cuopone,null=True,blank=True)
    def __str__(self):
        return f"{self.user}"
