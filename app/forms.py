from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.forms.widgets import PasswordInput,TextInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import PhotoCategory,PhotoGallery


class registerform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class loginform(AuthenticationForm):
    username=forms.CharField(widget=TextInput)
    password=forms.CharField(widget=PasswordInput)

class PhotoForm(ModelForm):
    class Meta:
        model=PhotoGallery
        fields='__all__'
        exclude=['user']
        
        
class CategoryForm(ModelForm):
    class Meta:
        model=PhotoCategory
        fields='__all__'
