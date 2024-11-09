from django.urls import path
from .views import *

urlpatterns = [
    path('',Template.as_view(), name='base_generic.html'),
    path('categories/',CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/',CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/',CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/',CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/',CategoryDeleteView.as_view(), name='category_delete'),
    path('products/',ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('product/create/',ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/',ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/',ProductDeleteView.as_view(), name='product_delete'),
    path('customers/',CustomerListView.as_view(), name='customer_list'),
    path('customer/<int:pk>/',CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/create/',CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/update/',CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete/',CustomerDeleteView.as_view(), name='customer_delete'),
    path('orders/',OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/',OrderDetailView.as_view(), name='order_detail'),
    path('order/create/',OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/update/',OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/',OrderDeleteView.as_view(), name='order_delete'),
]
