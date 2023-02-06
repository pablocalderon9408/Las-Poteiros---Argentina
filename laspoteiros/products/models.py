from django.db import models

from laspoteiros.utils.models import RestaurantModel
from slugify import slugify


class ProductCategory(RestaurantModel):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Product category: {self.name}"

    class Meta:
        verbose_name = "Product category"
        verbose_name_plural = "Product categories"


class Product(RestaurantModel):

    name = models.CharField(
        max_length=50,
        unique=True
        )

    slug_name = models.SlugField(max_length=200, unique=True, blank=True)

    description = models.CharField(
        max_length=500,
        null=True
    )

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="category"
    )

    main_image = models.FileField(
        upload_to='users/photos',
        null=True,
        blank=True
        )

    price = models.DecimalField(
        default=0.0,
        max_digits=10,
        decimal_places=2
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug_name:
            # Check existence
            self.slug_name = slugify(self.name, separator="-")
            if Product.objects.filter(slug_name=self.slug_name).exists():
                self.slug_name = f"{self.slug_name}-{self.pos_id}"
        return super().save(*args, **kwargs)


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

    class Meta:
        verbose_name_plural = "Product image variants"

    def __str__(self) -> str:
        return f"Variant image: {self.pk}"


class Unit(RestaurantModel):

    name = models.CharField(max_length=50)

    slug_name = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return f"Unit: {self.name}"

    class Meta:
        verbose_name_plural = "Units"

class Ingredient(RestaurantModel):

    name = models.CharField(max_length=50, unique=True)

    slug_name = models.SlugField(max_length=200, unique=True)

    measurement_unit = models.ForeignKey(
        Unit,
        null=True,
        on_delete=models.SET_NULL,
        related_name="ingredients"
    )

    def save(self):
        if not self.slug_name:
            self.slugify()
        super().save()

    def __str__(self) -> str:
        return f"Ingredient: {self.name}"

    class Meta:
        verbose_name_plural = "Ingredients"
