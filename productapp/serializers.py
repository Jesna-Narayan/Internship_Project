from rest_framework import serializers
from .models import Categorycloth
from .models import Productcloth
from .models import ProductVariant

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorycloth
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productcloth
        fields = '__all__'

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'      