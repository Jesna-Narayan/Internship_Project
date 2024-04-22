from django.urls import path
from deliveryapp.views import *

urlpatterns = [
    path('delivery/list',delivery_list,name='delivery_list'),
    path('order/list',OrderList.as_view(),name='order-list'),
    path('order/add/',OrderAdd.as_view(),name='order-add'),
    path('order/<int:order_id>/delete/',OrderDelete.as_view(),name='order-delete'),
    path('order/<int:order_id>/edit/',OrderEdit.as_view(),name='order-edit'),

]