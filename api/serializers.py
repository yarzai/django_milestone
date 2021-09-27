from rest_framework import serializers
from products.models import Product


class FirstSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'code',
                  'quantity', 'is_availible', 'image', 'category', 'created', 'user']
