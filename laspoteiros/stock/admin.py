from django.contrib import admin

from laspoteiros.stock.models import UnitOfMeasure as Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['created', 'id', 'name']
    search_fields = ["name"]