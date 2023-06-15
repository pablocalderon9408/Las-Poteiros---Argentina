"""Recipe models."""

# Django
from django.db import models

# Models
from laspoteiros.utils.models import RestaurantModel
from laspoteiros.products.models import Product, Ingredient


class Recipe(RestaurantModel):
    """Recipe model.

    Recipe model is used to store the recipes.
    """

    name = models.CharField(max_length=50)

    slug_name = models.SlugField(max_length=200, unique=True)

    description = models.CharField(max_length=500, null=True)

    products = models.ManyToManyField(Product)

    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self) -> str:
        return f"Recipe: {self.name}"

    class Meta:
        verbose_name_plural = "Recipes"
        verbose_name = "Recipe"
        app_label = "recipes"

    def save(self, *args, **kwargs):
        if not self.slug_name:
            # Check existence
            self.slug_name = slugify(self.name, separator="-")