from django.contrib import admin
from laspoteiros.orders.models import CartProduct

from laspoteiros.orders.models import Order, Cart


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['created', 'id', 'user', 'status']
    list_filter = ['created', 'id', 'user', 'status']
    readonly_fields = ['created', 'id', 'user', 'status']


class CartProductInLine(admin.TabularInline):
    model = CartProduct
    autocomplete_fields = ["cart"]
    list_display = ['cart', "product", "quantity", "price"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['created', 'id', 'user', 'is_active']
    inlines = [CartProductInLine, ]
    search_fields = ["cart"]
