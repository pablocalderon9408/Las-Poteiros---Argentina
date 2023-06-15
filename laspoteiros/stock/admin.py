import nested_admin

from django.contrib import admin


from laspoteiros.stock.models import UnitOfMeasure as Unit
from laspoteiros.stock.models import (
    IngredientContainer,
    IngredientStock,
    ProductStock,
    Purchases,
    IngredientPurchase,
    ProductPurchase,
    ProviderDeliveryDays,
    Provider
)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug_name']
    search_fields = ["name"]


@admin.register(IngredientContainer)
class IngredientContainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'weight']
    search_fields = ["name"]


@admin.register(IngredientStock)
class IngredientStockAdmin(admin.ModelAdmin):
    list_display = ['id', 'ingredient', 'unit', 'quantity']
    search_fields = ["ingredient__name"]


@admin.register(ProductStock)
class ProductStockAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'unit', 'quantity']
    search_fields = ["product__name"]


class ProductPurchaseInlineAdmin(admin.TabularInline):
    model = ProductPurchase
    list_display = ['product', 'unit', 'quantity']
    autocomplete_fields = ["product"]


class IngredientPurchaseInlineAdmin(admin.TabularInline):
    model = IngredientPurchase
    list_display = ['ingredient', 'unit', 'quantity']
    autocomplete_fields = ["ingredient"]


@admin.register(Purchases)
class PurchasesAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'provider', 'total_amount_paid', 'created']
    fields = ['date', 'total_amount_paid', 'provider']
    search_fields = ["product__name"]
    inlines = [ProductPurchaseInlineAdmin, IngredientPurchaseInlineAdmin]


class ProviderDeliveryDaysInline(nested_admin.NestedTabularInline):
    model = ProviderDeliveryDays
    autocomplete_fields = ["provider"]
    extra = 0


@admin.register(ProviderDeliveryDays)
class ProviderDeliveryDaysAdmin(admin.ModelAdmin):
    list_display = ["provider", "day", "hour", "is_active", "day_number"]


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    search_fields = ["name"]
    inlines = [ProviderDeliveryDaysInline]
