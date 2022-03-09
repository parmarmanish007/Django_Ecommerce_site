from django.contrib import admin

# Register your models here.
from.models import Student,Blog
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    class Meta:
        model=Student
        fields=['name','email','username','password']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Meta:
        model=Blog
        fields=['title','price','description','img']

    