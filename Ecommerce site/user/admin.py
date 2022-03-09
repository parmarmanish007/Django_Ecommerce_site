from django.contrib import admin

# Register your models here.
from .models import Student,Blog,Product,Order
@admin.register(Student,Blog,Product,Order)
class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model=Student
        fields=['id','name','email','contact','username','password']

class BlogAdmin(admin.ModelAdmin):
    class Meta:
        models=Blog
        fields=['item','image']

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model=Product
        fields=['pro_name','pro_image','price','descripation','blog_id']

class OrdertAdmin(admin.ModelAdmin):
    class Meta:
        model=Order
        fields=['sid','pid','quantity']