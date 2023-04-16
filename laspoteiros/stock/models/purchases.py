import time

# Utils
from laspoteiros.utils.models import RestaurantModel

# Models
from laspoteiros.stock.models import UnitOfMeasure

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


DAYS_CHOICES = [
    ('monday', _('Lunes')),
    ('tuesday', _('Martes')),
    ('wednesday', _('Miércoles')),
    ('thursday', _('Jueves')),
    ('friday', _('Viernes')),
    ('saturday', _('Sábado')),
    ('sunday', _('Domingo')),
]


class Provider(RestaurantModel):
    """Provider model.

    Provider model is used to store the information of the providers.
    """

    # Name
    name = models.CharField(
        'name',
        max_length=50,
        help_text='Name of the provider.'
    )

    # Phone
    phone = models.CharField(
        'phone',
        max_length=50,
        help_text='Phone of the provider.'
    )

    # Address
    address = models.CharField(
        'address',
        max_length=50,
        help_text='Address of the provider.'
    )


    class Meta:
        """Meta option."""

        verbose_name = 'provider'
        verbose_name_plural = 'providers'

    def __str__(self):
        """Return product name."""
        return f"{self.name}"


class ProviderDeliveryDays(RestaurantModel):
    """Provider delivery days model.

    Provider delivery days model is used to store the information of the
    delivery days of the providers.
    """

    # Provider
    provider = models.ForeignKey(
        'stock.Provider',
        on_delete=models.CASCADE,
        related_name='delivery_days'
    )

    day = models.CharField(
        'Delivery day',
        max_length=100,
        choices=DAYS_CHOICES,
        help_text='Day name.'
    )

    day_number = models.IntegerField(default=0, help_text='Day number monday is 0 and sunday 6.')

    hour = models.TimeField(
        'Delivery hour',
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        'Active',
        default=True,
        help_text='Set to false to disable a delivery day.'
    )


    def __str__(self):
        """Return users name."""
        return '{}|{}'.format(self.day, self.is_active)

    def save(self, *args, **kwargs):
        self.day_number = time.strptime(self.day, "%A").tm_wday
        return super().save(*args, **kwargs)

    class Meta:
        """Meta option."""

        verbose_name = 'provider delivery day'
        verbose_name_plural = 'provider delivery days'


class Purchases(RestaurantModel):
    """Purchases model.

    Purchases model is used to store the information of the purchases.

    This model will update the stock of the products and ingredients.
    """

    # Provider
    provider = models.ForeignKey(
        'stock.Provider',
        on_delete=models.CASCADE,
        related_name='purchases'
    )

    # Price
    total_amount_paid = models.PositiveIntegerField(
        'Total amount paid',
        default=0,
        help_text='Total invoice amount.'
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

    def __str__(self):
        """Return product name."""
        return f"{self.id}"


class ProductPurchase(RestaurantModel):
    """ProductPurchase model.

    ProductPurchase model is used to store the stock of the ingredients.
    """

    purchase = models.ForeignKey(
        'stock.Purchases',
        on_delete=models.CASCADE,
        related_name='product',
        null=True,
        blank=True,
    )

    # Product
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='purchase'
    )

    unit = models.ForeignKey(
        UnitOfMeasure,
        on_delete=models.CASCADE,
    )

    # Quantity
    quantity = models.PositiveIntegerField(
        'stock',
        default=0,
        help_text='Product quantity of the purchase.'
    )

    amount_paid = models.PositiveIntegerField(
        'price',
        default=0,
        help_text='Total amount paid for the product.',
        null=True,
        blank=True
    )

    class Meta:
        """Meta option."""

        verbose_name = 'product purchase'

    def __str__(self):
        """Return product name."""
        return f"{self.product.name} - {self.amount_paid}"


class IngredientPurchase(RestaurantModel):
    """IngredientPurchase model.

    IngredientPurchase model is used to store the stock of the ingredients.
    """

    purchase = models.ForeignKey(
        'stock.Purchases',
        on_delete=models.CASCADE,
        related_name='ingredient',
        null=True,
        blank=True,
    )

    ingredient = models.ForeignKey(
        'products.Ingredient',
        on_delete=models.CASCADE,
        related_name='purchase',
    )

    unit = models.ForeignKey(
        UnitOfMeasure,
        on_delete=models.CASCADE,
    )

    # Quantity
    quantity = models.PositiveIntegerField(
        'quantity',
        default=0,
        help_text='Ingredient quantity of the purchase.'
    )

    amount_paid = models.PositiveIntegerField(
        'price',
        default=0,
        help_text='Total amount paid for the ingredient.',
        null=True,
        blank=True
    )

    class Meta:
        """Meta option."""

        verbose_name = 'Ingredient purchase'

    def __str__(self):
        """Return product name."""
        return f"{self.ingredient.name} - {self.amount_paid}"