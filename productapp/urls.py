from django.urls import path
from productapp.views import *

urlpatterns =[
    path('category/list',category_list,name='category_list'),
    path('product/list',product_list,name='product_list'),
    path('ProductVariant/list',ProductVariant_list,name='ProductVariant_list'),
    path('category/<int:category_id>/products/',CategoryWithProduct.as_view(),name='Category-With-Product'),
]