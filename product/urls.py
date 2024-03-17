from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='index'),
    # path('create-product/', views.create_product, name='create-product'),
    path('create-product/<str:product_type>/', views.ProductCreateView.as_view(), name='create-product'),
    path('edit-product/<str:product_type>/<int:pk>/', views.ProductUpdateView.as_view(), name='edit-product'),
    path('delete-product/<int:pk>/', views.delete_product, name='delete-product'),
    # path('edit-product/<int:product_id>/', views.edit_product, name='edit-product'),
    path('your-products/', views.your_products, name='your-products'),
]