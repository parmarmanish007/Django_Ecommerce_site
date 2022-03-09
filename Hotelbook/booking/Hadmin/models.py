from django.db import models

# Create your models here.


class Area(models.Model):
    a_name = models.CharField(max_length=20)
    pincode = models.IntegerField()


class User(models.Model):
    unm=models.CharField(max_length=100)
    email=models.EmailField()
    pwd=models.CharField(max_length=8)
    cpwd=models.CharField(max_length=8)
    add=models.TextField()
    contact=models.IntegerField()
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)


class Detail(models.Model):
    nm=models.CharField(max_length=100)
    img=models.FileField()
    price=models.IntegerField()
    address=models.TextField()
    area1_id=models.ForeignKey(Area , on_delete=models.CASCADE)


class Gallary(models.Model):
    img1=models.FileField()
    name= models.CharField(max_length=20)
    detail_id = models.ForeignKey(Detail,on_delete=models.CASCADE)

class Booking(models.Model):
    date=models.DateField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    detail2_id=models.ForeignKey(Detail, on_delete=models.CASCADE, null=True)


class Wishlist(models.Model):
    date= models.DateField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    detail_id=models.ForeignKey(Detail, on_delete=models.CASCADE, null=True)


class contact1(models.Model):
    email2 = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    message = models.TextField()

class Feedback(models.Model):
    date = models.DateField()
    msg = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    detail_id = models.ForeignKey(Detail, on_delete=models.CASCADE)


