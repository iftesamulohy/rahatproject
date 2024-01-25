from django.contrib import admin

from coupon.models import Cuopone

# Register your models here.
@admin.register(Cuopone)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','code']