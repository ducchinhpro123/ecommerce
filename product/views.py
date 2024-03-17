from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from seller.models import Seller
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'product/list-product.html')


class ProductUpdateView(UpdateView):
    template_name = 'product/edit-product.html'
    success_url = reverse_lazy('index:index')

    def get_form_class(self):
        product_type = self.kwargs['product_type']
        if product_type == 'book':
            return BookForm
        else:
            return ProductForm

    def get_model(self):
        product_type = self.kwargs['product_type']
        if product_type == 'book':
            return Book
        else:
            return Product

    def get_queryset(self):
        product_type = self.kwargs['product_type']
        if product_type == 'book':
            return Book.objects.all()
        else:
            return Product.objects.all()

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        return product

    def form_valid(self, form):
        form.instance.seller = Seller.objects.get(user=self.request.user)
        return super().form_valid(form)


def your_products(request):
    seller = Seller.objects.get(user=request.user)
    products = Product.objects.filter(seller=seller)
    return render(request, 'product/your-products.html', {'products': products})


class ProductCreateView(CreateView):
    template_name = 'product/create-product.html'
    success_url = reverse_lazy('index:index')

    def get_form_class(self):
        product_type = self.kwargs['product_type']
        if product_type == 'book':
            return BookForm
        else:
            return ProductForm

    def get_model(self):
        product_type = self.kwargs['product_type']
        if product_type == 'book':
            return Book
        else:
            return Product

    def form_valid(self, form):
        form.instance.seller = Seller.objects.get(user=self.request.user)
        return super().form_valid(form)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    user = request.user
    if product.seller.user != user:
        return redirect('product:your-products')
    product.delete()
    return redirect('product:your-products')
