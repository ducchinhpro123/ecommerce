from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('register-seller/', views.register, name='register-seller'),
]
