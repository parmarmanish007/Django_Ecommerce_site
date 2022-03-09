from django.urls import path
from.import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.login),
    path('logout/',views.logout),
    path('email/',views.email),
    path('home/',views.home),
    path('product/',views.product),
    path('addcart/',views.addcart),
    path('cart/', views.cart),
    path('wishlist/',views.wishlist),
    path('view/<int:id>',views.view),
    path('product_details/<int:id>/',views.product_details),
    path('shop/',views.shop),
    path('shop_sub/<int:id>/',views.shop_sub),
    path('details/<int:id>/',views.details),
    path('add/<int:id>/',views.add),
    path('feedback/', views.feedback),
    path('wishlist_show/',views.wishlist_show),
    path('checkout/',views.checkout),
    path('remove_cart/<int:id>/',views.remove_cart),
    path('final_order/', views.final_order),
    
]
