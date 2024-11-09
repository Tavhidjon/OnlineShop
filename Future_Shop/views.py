from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from .models import *

class Template(TemplateView):
    template_name='base_generic.html'
    


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')
    fields='__all__'

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_form.html'
    success_url = reverse_lazy('category_list')
    fields='__all__'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')
    fields='__all__'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')
    fields='__all__'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'
    

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer_list')
    fields='__all__'

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer_list')
    fields='__all__'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')
    

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'
    

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')
    fields='__all__'

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')
    fields='__all__'

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

    
