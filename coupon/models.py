from django.db import models

from category.models import Category

# Create your models here.
class Cuopone(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField
    Free_shipping = models.BooleanField()
    OPTIONl = 'Fixed'
    OPTIONm = 'Percentage'
    CHOICES6 = (
        
        (OPTIONl, 'Fixed'),
        (OPTIONm, 'Percentage'), 
        
    )
    discount_type = models.CharField(max_length=50, choices=CHOICES6)
    amount = models.FloatField()
    category = models.ManyToManyField(Category)
    spent_limit = models.IntegerField()