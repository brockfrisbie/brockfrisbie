from django.urls import path
from . import views

urlpatterns = [
    path('', views.bitcoin_price, name='bitcoin_price'),
]