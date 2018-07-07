
from django.urls import path
from . import views

urlpatterns = [

    path('price/', views.price, name= 'price'),
    path('', views.home),
    ]