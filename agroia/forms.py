from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    CHOICES = (('', 'Choose the role'),('Administrator','Administrator'),('Agency','Agency'),('Executive', 'Executive'))
    role = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','role','email','password1','password2']

class UserChangeForm(UserChangeForm):
    CHOICES = (('', 'Choose the role'),('Administrator','Administrator'),('Agency','Agency'),('Executive', 'Executive'))
    role = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','role','email']

class ItemForm(forms.ModelForm):
    title = forms.CharField(max_length=99)
    detail = forms.CharField(max_length=499)
    method = forms.IntegerField()
    class Meta:
        model = Item
        fields = ['title','detail','image','method']
class MethodForm(forms.ModelForm):
    title = forms.CharField(max_length=99)
    detail = forms.CharField(max_length=499)
    class Meta:
        model = Method
        fields = ['title','detail','weights','script']
