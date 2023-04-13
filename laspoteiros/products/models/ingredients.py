# Django
from django.db import models

# Models
from laspoteiros.utils.models import RestaurantModel

from slugify import slugify

class Ingredient(RestaurantModel):
    """
    This model is used to store the ingredients.
    """

    name = models.CharField(max_length=50, unique=True)

    slug_name = models.SlugField(max_length=200, unique=True)

    def save(self):
        if not self.slug_name:
            self.slug_name = self.slugify()
        super().save()

    def __str__(self) -> str:
        return f"Ingredient: {self.name}"

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Ingredients"
        verbose_name = "Ingredient"
        app_label = "products"
