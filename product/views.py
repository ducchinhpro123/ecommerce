from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'product/list-product.html')


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index:index')
        else:
            return render(request, 'product/create-product.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'product/create-product.html', {'form': form})
