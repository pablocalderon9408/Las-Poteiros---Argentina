from django.db import models
from laspoteiros.products.models import Product
from laspoteiros.users.models import User

from laspoteiros.utils.models import RestaurantModel


class Cart(RestaurantModel):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        default=True,
    )

    def __str__(self) -> str:

        return super().__str__()


class CartProduct(RestaurantModel):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    quantity = models.IntegerField(
        default=0
    )

    price = models.FloatField(
        default=0
    )

    @property
    def total_price(self):
        return self.products * self.quantity


class Order(RestaurantModel):

    class StatusOptions(models.TextChoices):
        FINISHED = 'FINISHED', 'FINISHED'
        IN_PROGRESS = 'IN_PROGRESS', 'IN PROGRESS'
        UNAPPROBED = 'UNAPPROBED', 'UNAPPROBED'

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    status = models.CharField(
        max_length=25,
        choices=StatusOptions.choices,
        default=StatusOptions.UNAPPROBED,
    )
