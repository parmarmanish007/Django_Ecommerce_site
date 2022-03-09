from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.IntegerField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Blog(models.Model):
    item = models.CharField(max_length=20)
    image = models.FileField()


class Product(models.Model):
    pro_name =models.CharField(max_length=30) 
    pimage = models.FileField()
    price = models.IntegerField()
    description = models.TextField()
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Order(models.Model):
    sid=models.ForeignKey(Student, on_delete=models.CASCADE)
    pid=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity=models.IntegerField()

    def get_total_item_price(self):
        return self.quantity * self.pid.price


class Wishlist(models.Model):
    sid=models.ForeignKey(Student, on_delete=models.CASCADE)
    pid=models.ForeignKey(Product, on_delete=models.CASCADE, null=True)


class Feedback(models.Model):
    sid=models.ForeignKey(Student, on_delete=models.CASCADE)
    pid=models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    date=models.DateField()
    address=models.TextField()
    review=models.IntegerField()

class Billing(models.Model):
    user=models.ForeignKey(Student, on_delete=models.CASCADE)
    address=models.TextField(max_length=200)
    apprtment=models.TextField(max_length=200)
    country=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    zip=models.IntegerField()

class order_item(models.Model):
    billing=models.ForeignKey(Billing, on_delete=models.CASCADE, null=True)
    user=models.ForeignKey(Student, on_delete=models.CASCADE)
    item=models.ManyToManyField(Order)
    orderdate=models.DateField()
    ordered=models.BooleanField()

    def get_total(self):
        total = 0 
        for i in self.item.all():
            total += i.get_total_item_price()
        return total





class gallary(models.Model):
    image=models.FileField()
    pid=models.ForeignKey(Product, on_delete=models.CASCADE)

