from . import views
from django.urls import path, include

app_name = 'user'

urlpatterns = [
    path('login/', views.login_to, name='login'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('logout/', views.logout_from, name='logout'),
]
