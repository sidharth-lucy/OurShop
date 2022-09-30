
from cProfile import label
from dataclasses import field
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import (UserCreationForm , AuthenticationForm,UsernameField ,PasswordChangeForm ,
                                        PasswordResetForm , SetPasswordForm)
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext ,gettext_lazy as _ 

from .models import Customer

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields =['name' ,'locality' , 'city' , 'zipcode' ,'state']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'})
        }

class UserSetPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New Password' , strip=False ,
    widget=forms.PasswordInput(attrs={ 'autocomplete':'New-password' ,
    'class':'form-control'}) , help_text=password_validation.password_validators_help_text_html(),) 
                                    
    new_password2 = forms.CharField(label='Confirm Password' , strip=False ,
    widget=forms.PasswordInput(attrs={ 'autocomplete':'New-password' , 'class':'form-control'})) 
    

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField( label=_('Email'), max_length=254 ,widget=forms.EmailInput(attrs={
        'autocomplete':'email','class':'form-control'
    }))


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password' , strip=False ,
    widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password' , 'autofocus':True , 
    'class':'form-control'})) 

    new_password1 = forms.CharField(label='New Password' , strip=False ,
    widget=forms.PasswordInput(attrs={ 'autocomplete':'New-password' , 'autofocus':True , 
    'class':'form-control'}) , help_text=password_validation.password_validators_help_text_html(),) 
                                    

    new_password2 = forms.CharField(label='Confirm Password' , strip=False ,
    widget=forms.PasswordInput(attrs={ 'autocomplete':'New-password' , 'autofocus':True , 
    'class':'form-control'})) 

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True ,'class':'form-control'}))
    password = forms.CharField(label=_('Password') ,strip=False , widget=forms.PasswordInput(attrs={'autocomplete':'current-password' ,
    'class':'form-control'}))


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label = 'Email' ,required=True , widget= forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username' ,required=True , widget= forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields =['username','email','password1','password2']
        