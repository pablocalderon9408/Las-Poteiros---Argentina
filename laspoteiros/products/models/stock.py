# Django
from django.db import models

# Models
from laspoteiros.utils.models import RestaurantModel

from slugify import slugify


class UnitOfMeasure(RestaurantModel):
    """
    This model is used to store the units of measure.
    """
    name = models.CharField(max_length=50)

    slug_name = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return f"Unit: {self.name}"

    class Meta:
        verbose_name_plural = "Units"
        verbose_name = "Unit"
        app_label = "products"
