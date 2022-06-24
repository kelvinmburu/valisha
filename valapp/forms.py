from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

# Create your forms here
class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, label='',widget=forms.EmailInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Email'}))
    username =forms.CharField(max_length=200, label='',widget=forms.TextInput(attrs={'class': 'form-control mb-4','placeholder': 'Username'}))
    password1 = forms.CharField(max_length=200,label='',widget=forms.PasswordInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=200, label='',widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','placeholder': 'Confirm password'}))
    
    class Meta():
       model=User
       fields = ['email', 'username', 'password1', 'password2']
       

class UpdateProfileForm(ModelForm):
    bio = forms.CharField(max_length=200, label='Bio',widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
    pic = forms.FileField(max_length=200,label='Upload Profile Photo',widget=forms.FileInput(attrs={'class': 'form-control mb-4'}))
    
    class Meta():
        model = Profile
        fields = ['bio', 'pic']
        
