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

    converted_into_order = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return super().__str__()

    @property
    def total(self):
        total = 0
        for cart_product in self.cartproduct_set.all():
            total += cart_product.product.price * cart_product.quantity
        return total

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'is_active'],
                name='unique_active_cart'
            )
        ]


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
