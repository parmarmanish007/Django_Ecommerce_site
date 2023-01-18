from django.urls import path
from.import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.login, name='login'),
    path('register/',views.register,name='register'),
    path('blog/',views.blog_show,name='blog'),
    path('insert/',views.insert,name='insert'),
    path('blog_details/<int:id>/', views.blog_details),
    path('cart/',views.cart,name='cart'),
    path('contact/',views.contact,name='contact'),
    path('chekout/',views.chekout,name='chekout'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('shop/',views.shop,name='shop'),
    path('single/',views.single,name='single'),
    path('sidebar/',views.sidebar,name='sidebar'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update),
    

]

