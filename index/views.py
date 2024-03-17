from django.shortcuts import render
from product.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()

    return render(request, 'index/index.html', {'products': products})
