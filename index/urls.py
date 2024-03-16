from . import views
from django.urls import path, include

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
]