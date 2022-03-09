from django import forms
from .models import User, Area, Detail, Gallary, Booking, Wishlist, contact1,Feedback


class areaForm (forms.ModelForm):
    class Meta:
        model = Area
        fields = ['a_name', 'pincode']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['unm', 'email', 'pwd', 'cpwd', 'add', 'contact', 'area_id']

class detailForm (forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['nm', 'img', 'price', 'address', 'area1_id']

class gallaryForm (forms.ModelForm):
    class Meta:
        model = Gallary
        fields = ['img1','name', 'detail_id']

class bookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'user_id', 'detail2_id']

class wishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields =['date', 'user_id','detail_id']

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact1
        fields = ['email2', 'subject', 'message']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['date','msg', 'user_id', 'detail_id']