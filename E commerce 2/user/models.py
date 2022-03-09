from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    roll=models.IntegerField()
    email=models.EmailField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Blog(models.Model):
    item=models.CharField(max_length=30)
    image=models.FileField()

class Product(models.Model):
    pname=models.CharField(max_length=20)
    pimage=models.FileField()
    pdescription=models.TextField()
    pprice=models.IntegerField()
    pid=models.ForeignKey(Blog,on_delete=models.CASCADE)

class Order(models.Model):
    sid=models.ForeignKey(Student, on_delete=models.CASCADE)
    pid=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

class Wishlist(models.Model):
    sid=models.ForeignKey(Student, on_delete=models.CASCADE)
    pid=models.ForeignKey(Product, on_delete=models.CASCADE)


