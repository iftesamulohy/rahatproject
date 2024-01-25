from django.db import models
from django.utils.text import slugify
# Create your models here.

class SubsubCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload", blank=True, null=True)
    sub_category = models.ManyToManyField(SubsubCategory)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="upload", blank=True, null=True)
    sub_category = models.ManyToManyField(SubCategory)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"