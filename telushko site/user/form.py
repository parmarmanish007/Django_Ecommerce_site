from django import forms
from.models import Student,Blog

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=['name','email','username','password']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields=['title','price','description','img']
    # def get_total(self):
    #     total = self.price * self quantity
    #     return total