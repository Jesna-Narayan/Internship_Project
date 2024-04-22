from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from.models import *
from .serializers import *
from rest_framework import status

@api_view(['GET'])
def delivery_list(request):
    if request.method == 'GET':
        delivery = Delivery.objects.all()
        serializer = DeliverySerializer(delivery,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class OrderList(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class OrderAdd(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all() 
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDelete(APIView):
    def get(self, request, order_id, format=None):
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, order_id, format=None):
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderEdit(APIView):
    def get(self, request, order_id, format=None):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, order_id, format=None):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    