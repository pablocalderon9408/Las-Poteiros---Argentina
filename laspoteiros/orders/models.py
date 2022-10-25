from django.db import models
from laspoteiros.products.models import Addition, Product
from laspoteiros.users.models import User

from laspoteiros.utils.models import RestaurantModel
from laspoteiros.products.models import RestaurantModel


class ShoppingCart(RestaurantModel):

    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    additions = models.ForeignKey(
        Addition,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    quantity = models.IntegerField(
        default=1,
        blank=False,
        null=False
    )

    def __str__(self) -> str:

        return super().__str__()

    @property
    def total_price(self):
        return self.products * self.quantity


class Order(RestaurantModel):

    class StatusOptions(models.TextChoices):
        FINISHED = 'FINISHED', 'FINISHED'
        IN_PROGRESS = 'IN_PROGRESS', 'IN PROGRESS'
        UNAPPROBED = 'UNAPPROBED', 'UNAPPROBED'

    shopping_cart = models.ForeignKey(
        ShoppingCart,
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
