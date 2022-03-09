from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index),
    path('create_user/', views.create_user),
    path('table/', views.table),

    path('areas/', views.areas),
    path('details/', views.details),
    path('gallary/', views.gallary),
    path('booking/', views.booking),
    path('wishlists/', views.wishlists),



]