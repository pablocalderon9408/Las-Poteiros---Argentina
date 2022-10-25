from django.db import models

from laspoteiros.utils.models import RestaurantModel

# Create your models here.

class AdditionCategory(RestaurantModel):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Addition Category: {self.name}"


class ProductCategory(RestaurantModel):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Product category: {self.name}"


class Addition(RestaurantModel):

    name = models.CharField(max_length=50)

    category = models.ForeignKey(
        AdditionCategory,
        on_delete = models.CASCADE,
        related_name = "category"
    )

    image = models.FileField(
        upload_to='users/photos', 
        null=True, 
        blank=True
        )

    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"Addition: {self.name}"


class Product(RestaurantModel):

    name = models.CharField(
        max_length=50
        )

    category = models.ForeignKey(
        ProductCategory,
        on_delete = models.CASCADE,
        related_name = "category"
    )

    main_image = models.FileField(
        upload_to='users/photos', 
        null=True, 
        blank=True
        )

    price = models.FloatField(
        default=0
        )

    def __str__(self) -> str:
        return f"Product: {self.name}"


class ProductImageVariants(RestaurantModel):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
        )

    image = models.FileField(
        upload_to='users/photos', 
        null=True, 
        blank=True
        )

    def __str__(self) -> str:
        return f"Variant image: {self.pk}"