from rest_framework import serializers
from products.models import Product
from wishcart.models import Cart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductSerializer()  # Assuming ProductSerializer is defined for the Product model

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'color', 'size', 'quantity', 'vendor']
class CartSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'color', 'size', 'quantity', 'vendor']