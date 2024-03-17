from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-product/', views.create_product, name='create-product'),
]