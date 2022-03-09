from django import forms
from.models import Student,Blog,Product,Order,Feedback,Wishlist,Billing,order_item,gallary

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','contact','username','password']

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['item','image']

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['pro_name','pimage','price','description','blog_id']

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['quantity','sid','pid']

class WishlistForm(forms.ModelForm):
    class Meta:
        model=Wishlist
        fields=['sid','pid']
        

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['date','sid','pid','review']
        widgets = {'review': forms.NumberInput(attrs={'class': 'Stars'})}
        labels = {'review': 'Note /5'}

class BillingForm(forms.ModelForm):
    class Meta:
        model=Billing
        fields=['user','address','apprtment','country','phone','email','zip']
class order_itemForm(forms.ModelForm):
    class Meta:
        model=order_item
        fields=['billing','user','item','orderdate','ordered']


class gallaryForm(forms.ModelForm):
    class Meta:
        model=gallary
        fields=['image','pid']



