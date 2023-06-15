# Django Rest Framework
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework import status

# Serializers
from laspoteiros.products.api.serializers import ProductSerializer

# Permissions
from rest_framework.permissions import AllowAny

# Models
from laspoteiros.products.models import Product


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """Product view set."""

    queryset = Product.objects.all()
    lookup_field = "pk"
    lookup_url_kwarg = "pk"
    serializer_class = ProductSerializer
    permissions = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a product."""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)