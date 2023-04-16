
# Utils
from laspoteiros.utils.models import RestaurantModel

# Django
from django.db import models


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
        # app_label = "stock"


class IngredientStock(RestaurantModel):
    """Stock model.

    IngredientStock model is used to store the stock of the ingredients.
    """
    # Product
    ingredient = models.ForeignKey(
        'products.Ingredient',
        on_delete=models.CASCADE,
        related_name='stock'
    )

    unit = models.ForeignKey(
        UnitOfMeasure,
        on_delete=models.CASCADE,
    )

    # Quantity
    quantity = models.PositiveIntegerField(
        'stock',
        default=0,
        help_text='Stock of the product.'
    )

    # Stock min
    stock_min = models.PositiveIntegerField(
        'stock min',
        default=0,
        help_text='Minimum stock of the product.'
    )

    # Stock max
    stock_max = models.PositiveIntegerField(
        'stock max',
        default=0,
        help_text='Maximum stock of the product.'
    )

    container = models.ForeignKey(
        'IngredientContainer',
        on_delete=models.CASCADE,
        related_name='stock',
        null=True,
        blank=True,
    )

    class Meta:
        """Meta option."""

        verbose_name = 'ingredient stock'
        ordering = ['ingredient__name']

    def __str__(self):
        """Return ingredient name."""
        return f"{self.ingredient.name} - {self.quantity} {self.unit.name}"


class ProductStock(RestaurantModel):
    """Stock model.

    ProductStock model is used to store the stock of the ingredients.
    """

    # Product
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='stock'
    )

    unit = models.ForeignKey(
        UnitOfMeasure,
        on_delete=models.CASCADE,
    )

    # Quantity
    quantity = models.PositiveIntegerField(
        'stock',
        default=0,
        help_text='Stock of the product.'
    )

    # Stock min
    stock_min = models.PositiveIntegerField(
        'stock min',
        default=0,
        help_text='Minimum stock of the product.',
        null=True,
        blank=True,
    )

    # Stock max
    stock_max = models.PositiveIntegerField(
        'stock max',
        default=0,
        help_text='Maximum stock of the product.',
        null=True,
        blank=True,
    )

    class Meta:
        """Meta option."""

        verbose_name = 'product stock'
        ordering = ['product__name']

    def __str__(self):
        """Return product name."""
        return f"{self.product.name} - {self.quantity} {self.unit.name}"


class IngredientContainer(RestaurantModel):
    """Ingredient container model.

    IngredientContainer model is used to store the information of the containers
    of the ingredients.

    Ingredients are stored in containers, and during the stock management,
    containers are weighted to know the quantity of the ingredient in the
    container.
    """
    name = models.CharField(max_length=50)

    slug_name = models.SlugField(max_length=200, unique=True)

    # Quantity
    weight = models.PositiveIntegerField(
        'weight',
        default=0,
        help_text='Weight of the container in gr.'
    )

    class Meta:
        """Meta option."""

        verbose_name = 'container'
        verbose_name_plural = 'containers'

    def __str__(self):
        """Return ingredient name."""
        return f"{self.name}"
