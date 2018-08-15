
from django.urls import path
from . import views
from bitcoin.views import MyView

urlpatterns = [

    path('price/', views.price, name= 'price'),
    path('home/', views.home,name='home'),
    path('about/', MyView.as_view()),
    ]