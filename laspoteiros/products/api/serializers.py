# Django rest framework
from rest_framework import serializers

# Models
from laspoteiros.products.models import Product, ProductImageVariants


class ProductImageVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageVariants
        fields = ('image', )


class ProductSerializer(serializers.ModelSerializer):

    images = ProductImageVariantsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'category', 'main_image', 'images')
