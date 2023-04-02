from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from . import models
from . import forms, common
# Create your views here.

## index view
def index(request):
    return render(request, 'index.html')

## Sign in
def signin(request):
    loginForm = forms.UserLoginForm()

    if request.method == "POST":
        loginForm = forms.UserLoginForm(request.POST)
        if loginForm.is_valid():
            email = loginForm.cleaned_data['email']
            password = loginForm.cleaned_data['password']

            try:
                user_info = models.UserInfo.objects.get(email=email)
                username = user_info.user.username
                user = authenticate(username=username, password=password)
                if user is not None:
                    return HttpResponseRedirect('/logined')
                else:
                    return HttpResponseRedirect('/')
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'auth/login.html', {'loginForm': loginForm})

## Sign Up
def signup(request):
    userForm = forms.UserRegisterForm()
    infoForm = forms.UserInfoForm()

    if request.method == 'POST':
        userForm = forms.UserRegisterForm(request.POST)
        infoForm = forms.UserInfoForm(request.POST)

        if userForm.is_valid() and infoForm.is_valid():
            user = User.objects.create_user(userForm.cleaned_data['username'],
                userForm.cleaned_data['email'],
                userForm.cleaned_data['password'])
            user.save()

            info = models.UserInfo(user=user,
                email=common.emailGenerate(),
                phone=infoForm.cleaned_data['phone'],
                country=infoForm.cleaned_data['country'])
            info.save()

        return HttpResponseRedirect('/')
    
    return render(request, 'auth/register.html', { 'userForm': userForm, 'infoForm': infoForm })

## About Us Page
def about_us(request):
    return render(request, 'about.html', {'title': 'About Us', 'menu': 'about'})

## Price Plans
def pricing_plans(request):
    return render(request, 'price.html', {'title': 'Pricing Plans', 'menu': 'price'})

## Contact
def contact_us(request):
    contactForm = forms.ContactForm()
    return render(request, 'contact.html', {'contactForm': contactForm, 'title': 'Contact Us', 'menu': 'contact'})

## Contact
def contact_us_2(request):
    return render(request, 'contact.html', {'title': 'Contact Us', 'menu': 'contact'})