from django.contrib import admin

from orders.models import Order, OrderedProduct

# Register your models here.

@admin.register(OrderedProduct)
class OrderedProductAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user']