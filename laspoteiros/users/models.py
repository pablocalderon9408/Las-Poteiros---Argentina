"""User authentication model"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from laspoteiros.utils.models import RestaurantModel


class User(RestaurantModel, AbstractUser):
    """This model holds the user's information."""

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    email = models.EmailField(
        help_text="email address",
        unique=True,
        error_messages={
            "unique": "A user with that email already exists"
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be enered in the format: +999999999999. Up to 15 digits allowed"
    )

    phone_number = models.CharField(max_length=17, blank=True, validators=[phone_regex])

    is_client = models.BooleanField(
        "client",
        default=True,
        help_text=(
            "Help easily distinguish users and perform queries."
            "Clients are the main type of users"),
    )

    is_verified = models.BooleanField(
        "verified",
        default=True,
        help_text="Set to true when the user have verified its email address."
    )