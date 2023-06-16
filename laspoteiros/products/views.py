# Products views.

# Django
from typing import Any, Dict
from django.views.generic import TemplateView, FormView

# Models
from laspoteiros.products.models import Product


class ProductListView(TemplateView):
    """Product list view."""

    model = Product
    template_name ="index.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add extra context."""
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category__name="Primeros")
        context["additions"] = Product.objects.filter(category__slug_name="adiciones")
        return context


class ProductDetailView(TemplateView):
    """Product detail view."""

    model = Product
    template_name ="product-tab.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Add extra context."""
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.get(pk=self.kwargs["pk"])
        return context
