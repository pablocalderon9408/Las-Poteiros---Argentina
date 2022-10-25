from django.contrib import admin

from laspoteiros.products.models import ProductCategory, AdditionCategory, Addition, Product

# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(AdditionCategory)
class AdditionCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Addition)
class AdditionAdmin(admin.ModelAdmin):
    list_display = ['name', "price"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', "price"]



