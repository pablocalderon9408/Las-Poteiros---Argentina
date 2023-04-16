# Django
from django.core.management.base import BaseCommand

# Models
from laspoteiros.products.models import ProductCategory, Product, Ingredient
from laspoteiros.stock.models import UnitOfMeasure as Unit


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Handle command usage."""

        # Create categories
        categories = [
            "Entrantes",
            "Primeros",
            "Segundos",
            "Postres",
            "Bebidas",
            "Otros"
        ]

        for category in categories:
            ProductCategory.objects.get_or_create(name=category)

        # Create units
        units = [
            "Kg",
            "g",
            "L",
            "ml",
            "Unidad",
            "Paquete"
        ]

        for unit in units:
            Unit.objects.get_or_create(name=unit, slug_name=unit.lower())

        # Create ingredients
        ingredients = [
            "Tomate",
            "Lechuga",
            "Queso",
            "Jamón",
            "Pimiento",
            "Cebolla",
            "Huevo",
            "Pan",
            "Carne",
            "Patatas",
            "Cerveza",
            "Vino",
            "Agua",
            "Aceite",
            "Sal",
            "Azúcar",
            "Harina",
            "Pasta",
            "Arroz",
            "Café",
            "Chocolate",
            "Mantequilla",
            "Nata",
            "Cebolla",
            "Ajo",
            "Perejil",
            "Pimienta",
            "Nuez moscada",
            "Canela",
            "Clavo",
            "Jengibre",
            "Cúrcuma",
            "Pimienta negra",
            "Pimienta blanca"
        ]

        for ingredient in ingredients:
            Ingredient.objects.get_or_create(slug_name=ingredient.lower(), defaults={"name": ingredient})