from django.contrib import admin

from laspoteiros.products.models import Product, ProductCategory, ProductImageVariants


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductImageVariantsInLine(admin.TabularInline):
    model = ProductImageVariants
    autocomplete_fields = ["product"]
    list_display = ['product', "image"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', "price"]
    search_fields = ["name", "price"]
    inlines = [ProductImageVariantsInLine]
