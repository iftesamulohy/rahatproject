from django.contrib import admin

from products.models import Brand, Color, Images, Product, ProductReviews, Size, Unit

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['filename']
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']