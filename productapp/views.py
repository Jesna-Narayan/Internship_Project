from django.shortcuts import render
# Create your views here.

from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        category = Categorycloth.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        category = Productcloth.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def ProductVariant_list(request):
    if request.method == 'GET':
        category = ProductVariant.objects.all()
        serializer = ProductVariantSerializer(category,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class CategoryWithProduct(APIView):
    def get(self, respect,category_id, format=None):
        try:
            category = Categorycloth.objects.get(id=category_id)
        except Categorycloth.DoesNotExist:
            return Response({'error': 'Category not found '}, status=status.HTTP_404_NOT_FOUND)
        
        category_serializer = CategorySerializer(category)
        products = Productcloth.objects.filter(category=category)
        final_data = []

        for product in products:
           
           products_serializer = ProductSerializer(product)
           product_variant = ProductVariant.objects.filter(product=product)
           variant_serializer = ProductVariantSerializer(product_variant,many=True)

           product_data = products_serializer.data
           product_data['variant']=variant_serializer.data

           final_data.append(product_data)
       
           

        response_data ={
            'category':category_serializer.data,
           'products':final_data
        }

        return Response(response_data,status=status.HTTP_200_OK)

# Create your views here.
