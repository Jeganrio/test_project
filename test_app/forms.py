from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from test_app.models import Register

class RegisterForm(UserCreationForm):
    username=forms.CharField(max_length=100)
    age = forms.IntegerField(required=True)
    photo = forms.ImageField(required=False)
    email=forms.EmailField(required=True)
    password1=forms.CharField(max_length=100)
    password2=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['username','age','photo','email','password1','password2']
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

