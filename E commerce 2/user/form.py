from django import forms
from.models import Student,Blog,Product,Order,Wishlist

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','roll','email','username','password']

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['item','image']

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['pname','pimage','pdescription','pprice','pid']

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['sid','pid','quantity']

class WishlistForm(forms.ModelForm):
    class Meta:
        model=Wishlist
        fields=['sid','pid']