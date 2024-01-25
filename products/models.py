from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from category.models import Category, SubCategory, SubsubCategory
# Create your models here.
class Images(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    filename = models.CharField(max_length=300)
    image = models.ImageField(upload_to="upload/")
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return None
    def __str__(self):
        return f"{self.filename}"
class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"
class Unit(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
class Brand(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="upload/")
    def __str__(self):
        return f"{self.name}"
class Size(models.Model):
    name = models.CharField(max_length=50)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE,null=True,blank=True)
    value = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.name}"
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    OPTION_a = 'New Arrival'
    OPTION_b = 'Feature Product'
    OPTION_c = 'Hot Product'
    CHOICES2 = (
        (OPTION_a, 'New Arrival'),
        (OPTION_b, 'Feature Product'),
        (OPTION_c, 'Hot Product'), 
        
    )
    type = models.CharField(max_length=50, choices=CHOICES2,blank=True,null=True)
    category = models.ManyToManyField(Category)
    sub_category = models.ManyToManyField(SubCategory)
    sub_Sub_category = models.ManyToManyField(SubsubCategory)
    brand = models.ManyToManyField(Brand,null=True,blank=True)
    color = models.ManyToManyField(Color,null=True,blank=True)
    size = models. ManyToManyField(Size,null=True,blank=True)
    short_descriptions = models.TextField()
    long_description = models.TextField()
    image = models.ManyToManyField(Images)
    videos = models.URLField(null=True,blank=True)
    price = models.FloatField()
    offer_price = models.FloatField()
    quantity = models.IntegerField()
    in_stock = models.BooleanField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}"
class ProductReviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,unique=True)
    title = models.CharField(max_length=200,null=True,blank=True)
    text = models.TextField(max_length=1000)
    def __str__(self):
        return f"{self.user}"