from django.contrib import admin

from wishcart.models import Cart, Wishlist

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user']