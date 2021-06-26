from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from basic_app.models import UserProfileinfo

class Userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileinfo
        fields=('portfolio_site','profile_pic')