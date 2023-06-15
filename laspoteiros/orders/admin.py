from django.contrib import admin
from laspoteiros.orders.models import Order, Cart, CartProduct


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['created', 'id', 'user', 'status']
    list_filter = ['created', 'id', 'user', 'status']
    readonly_fields = ['created', 'id', 'user', 'status']


class CartProductInLine(admin.TabularInline):
    model = CartProduct
    autocomplete_fields = ["cart"]
    list_display = ["product", "quantity", "product__category__name"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_active', 'total', 'created']
    readonly_fields = ['total']
    inlines = [CartProductInLine, ]
    search_fields = ["cart"]
