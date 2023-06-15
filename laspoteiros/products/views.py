# Products views.

# Django
from django.views.generic import ListView

# Models
from laspoteiros.products.models import Product


class ProductListView(ListView):
    """Product list view."""

    model = Product
    template_name = "base.html"
    context_object_name = "products"
