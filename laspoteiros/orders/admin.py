from django.contrib import admin

from laspoteiros.orders.models import Order, ShoppingCart
from laspoteiros.products.models import Product, Addition

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['created', 'id', 'user', 'status']
    list_filter = ['created', 'id', 'user', 'status']
    readonly_fields = ['created', 'id', 'user', 'status']


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['created', 'id', 'products', 'additions', 'quantity']
