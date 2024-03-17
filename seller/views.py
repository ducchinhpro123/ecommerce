from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('index:index')
        else:
            return render(request, 'seller/register-seller.html', {'form': form})
    else:
        form = SellerForm(user=request.user)
        return render(request, 'seller/register-seller.html', {'form': form})
