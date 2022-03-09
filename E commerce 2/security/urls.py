from django.urls import path
from.import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('home/',views.home),
    path('product_details/<int:id>/',views.product_details),
    path('addcart/',views.addcart),
    path('cart/',views.cart),
    path('wishlist/',views.wishlist),
    path('wishlist_show/',views.wishlist_show),
    path('shop/',views.shop),
    path('shop_sub/<int:id>/',views.shop_sub),
    path('details/<int:id>/',views.details),
    
]
