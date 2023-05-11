# Products views.

# Django
from django.views.generic import ListView, DetailView

# Models
from laspoteiros.products.models import Product, ProductCategory


class ProductListView(ListView):
    """Product list view."""

    model = Product
    template_name = "base.html"
    context_object_name = "products"
