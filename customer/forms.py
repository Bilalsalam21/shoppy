from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from api.models import Products,MyProducts


class RegistraionForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

    
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()


class ProductForm(forms.ModelForm):

    class Meta:
        model=Products
        fields="__all__"


class MyProductForm(forms.ModelForm):

    class Meta:
        model=MyProducts
        fields="__all__"

class ProductUpdateForm(forms.ModelForm):

    class Meta:
        model:Products
        fields="__all__"