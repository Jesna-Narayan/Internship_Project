from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

@api_view()
def hello_world(request):
    return Response({"message":"Hello,world!"})

@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        category =Category.objects.all()
        serializer =CategorySerializers(category,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        product =Product.objects.all()
        serializer =ProductSerializers(product,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def category_add(request):
    if request.method == 'GET':
        categories=Category.objects.all()
        serializer =CategorySerializers(categories,many = True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET','POST'])
def product_add(request):
    if request.method == 'GET':
        product=Product.objects.all()
        serializer =ProductSerializers(product,many = True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET'])
def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializers(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method ==  'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'DELETE'])
def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializers(category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method ==  'GET':
        serializer = CategorySerializers(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def category_edit(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializers(category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = CategorySerializers(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def product_edit(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = ProductSerializers(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def category_update(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializers(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = CategorySerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def product_update(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializers(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










