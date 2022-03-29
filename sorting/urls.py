from django.urls import path, include
from . import views

app_name = 'sort'
urlpatterns = [
    path('clothing/', views.clothing, name='clothing'),
    path('electronics/', views.electronics, name='electronics'),
    path('homeware/', views.homeware, name='homeware'),
    path('other/', views.other, name='other'),
    path('clothing_estore/', views.clothing_estore, name='clothing_estore'),
    path('electronics_estore/', views.electronics_estore, name='electronics_estore'),
    path('homeware_estore/', views.homeware_estore, name='homeware_estore'),
    path('other_estore/', views.other_estore, name='other_estore'),
    path('cosmetics_estore/', views.cosmetics_estore, name='cosmetics_estore'),
    path('vehicles_estore/', views.vehicles_estore, name='vehicles_estore'),


]