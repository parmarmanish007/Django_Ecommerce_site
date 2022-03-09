from django.urls import path

from . import views

urlpatterns = [
    path('view/', views.show),
    path('contact/', views.con),
    path('booking/', views.booking),
    path('booking_show/', views.booking_show),
    path('register/', views.register),
    path('about/', views.about),
    path('send/', views.send),
    path('all_gallary/', views.all_gallary),
    path('login/', views.login),
    path('logout/', views.logout),
    path('delete/<int:id>/', views.delete),
    path('hotel_detail/', views.hotel_detail),
    path('show_detail/<int:id>/', views.show_detail),
    path('wishlist_add/', views.wishlist_add),
    path('wishlist_show/', views.wishlist_show),
    path('feedback/', views.feedback),






]