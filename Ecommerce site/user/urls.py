from django.urls import path
from.import views

urlpatterns = [
    path('home/',views.home),
    path('basic/',views.basic,name='basic'),
    path('table/',views.table,name='table'),
    path('insert/',views.insert,name='insert'),
    path('blogtable/',views.blogtable,name='blogtable'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('blogedit/<int:id>/',views.blogedit,name='blogedit'),
    path('blogupdate/<int:id>/',views.blogupdate,name='blogupdate'),
    path('blogdelete/<int:id>/',views.blogdelete,name='blogdelete'),
    path('product/',views.product,name='product'),
    path('product_table/',views.product_table,name='product_table'),
    path('product_delete/<int:id>/',views.product_delete,name='product_delete'),
    path('product_edit/<int:id>/',views.product_edit,name='product_edit'),
    path('product_update/<int:id>/',views.product_update,name='product_update'),
    path('gallary/',views.gallary_add),
    path('gallary_table/',views.gallary_table)
    


]

