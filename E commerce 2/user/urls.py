from django.urls import path
from.import views

urlpatterns = [
    path('index/',views.index),
    path('basic_element/',views.basic_element),
    path('formtable/',views.formtable),
    path('formedit/<int:id>/',views.formedit),
    path('formupdate/<int:id>/',views.formupdate),
    path('formdelete/<int:id>/',views.formdelete),
    path('blog_element/',views.blog_element),
    path('blog_table/',views.blog_table),
    path('blog_edit/<int:id>/',views.blog_edit),
    path('blog_update/<int:id>/',views.blog_update),
    path('blog_delete/<int:id>/',views.blog_delete),
    path('product/',views.product),
    path('product_table/',views.product_table),
    path('product_edit/<int:id>/',views.product_edit),
    path('product_update/<int:id>/',views.product_update),
    path('product_delete/<int:id>/',views.product_delete),
]
