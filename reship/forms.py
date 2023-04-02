from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .common import countrylist
from . import models

# Create Forms

## Login Form
class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length = 100, 
        required = True, 
        widget = forms.TextInput(attrs = {
                'placeholder': 'Email Address' }))
    
    password = forms.CharField(max_length = 100, 
        required = True, 
        widget = forms.PasswordInput(attrs = { 
            'placeholder': 'Password',
            'class': 'form-control' }))

## Register Form
class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length = 200, 
        widget = forms.TextInput(attrs = { 
            'placeholder': 'Name', 
            'required': 'true', 
            'class': 'form-control' }))
    
    email = forms.EmailField(max_length = 100, 
        required = True)
    
    password = forms.CharField(max_length = 50, 
        required = True, 
        widget = forms.PasswordInput(attrs = {
            'placeholder': 'Password', 
            'class': 'form-control' }))

## User Info Form
class UserInfoForm(forms.Form):
    email = forms.EmailField(max_length = 100, 
        required = True, 
        widget = forms.EmailInput(attrs={
            'placeholder': 'Email Address', 
            'class': 'form-control'}))
    
    country = forms.ChoiceField(choices = countrylist, 
        required=True)
    
    phone = forms.CharField(max_length = 20, 
        widget = forms.TextInput(attrs={
            'placeholder': 'phone', 
            'class': "form-control", 
            'autocomplete': 'tel'}))

## Contact Form
class ContactForm(forms.Form):
    name = forms.CharField(max_length = 200, 
        label = 'NAME: ', 
        required = True, 
        widget = forms.TextInput(attrs = {
            'placeholder': 'Name', 
            'class': 'form-control'}))
    
    email = forms.EmailField(max_length = 100, 
        label='EMAIL: ', 
        required=True, 
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address', 
            'class': 'form-control'}))
    
    phone = forms.CharField(max_length = 20, 
        label = 'PHONE: ', 
        widget = forms.TextInput(attrs={
            'placeholder': 'phone', 
            'class': "form-control", 
            'autocomplete': 'tel'}))
    
    message = forms.CharField(label = 'MESSAGE: ', 
        widget=forms.Textarea(attrs={
            'cols': 25, 
            'rows': 3, 
            'class': 'form-control'}))
