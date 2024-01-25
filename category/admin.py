from django.contrib import admin

from category.models import Category, SubCategory, SubsubCategory

# Register your models here.
@admin.register(SubsubCategory)
class SubsubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']