
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
        default="Raw container"
    )

    class Meta:
        """Meta option."""

        verbose_name = 'stock'
        verbose_name_plural = 'stocks'
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
        help_text='Minimum stock of the product.'
    )

    # Stock max
    stock_max = models.PositiveIntegerField(
        'stock max',
        default=0,
        help_text='Maximum stock of the product.'
    )

    class Meta:
        """Meta option."""

        verbose_name = 'stock'
        verbose_name_plural = 'stocks'
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
        ordering = ['ingredient__name']

    def __str__(self):
        """Return ingredient name."""
        return f"{self.ingredient.name} - {self.quantity} {self.container.name}"

class Purchases(RestaurantModel):
    """Purchases model.

    Purchases model is used to store the information of the purchases.

    This model will update the stock of the products and ingredients.
    """

    # Ingredient
    ingredients = models.ManyToManyField(
        'products.Ingredient',
        related_name='purchases'
    )

    # Product
    products = models.ManyToManyField(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='purchases'
    )

    # Quantity
    quantity = models.PositiveIntegerField(
        'quantity',
        default=0,
        help_text='Quantity of the product.'
    )

    # Price
    price = models.PositiveIntegerField(
        'price',
        default=0,
        help_text='Price of the product.'
    )

    # Date: Created date doesn't work as some purchases are done in the past
    date = models.DateField(
        'date',
        auto_now=False,
        auto_now_add=False,
        help_text='Date of the purchase.'
    )

    class Meta:
        """Meta option."""

        verbose_name = 'purchase'
        verbose_name_plural = 'purchases'
        ordering = ['product__name']

    def __str__(self):
        """Return product name."""
        return f"{self.product.name} - {self.quantity} {self.product.unit.name}"
    
    @property
    def total_price(self):
        """Take into account products and ingredients."""
        products = self.products.all()
        ingredients = self.ingredients.all()
        total_ingredient_price = sum([ingredient.price for ingredient in ingredients])
        total_product_price = sum([product.price for product in products])
        return total_ingredient_price + total_product_price
    
