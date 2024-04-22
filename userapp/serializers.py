from rest_framework import serializers
from .models import Category
from .models import Product

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'