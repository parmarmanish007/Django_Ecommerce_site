from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    class Meta:
        db_table='student'
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.TextField()
    img=models.FileField()
    
    class Meta:
        db_table='blog'
class orderitem(models.Model):
    item=models.ForeignKey(Blog, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total(self):
        total = 0
        for i in self.item.all():
            total += i.get_total_item_price()
        return total

