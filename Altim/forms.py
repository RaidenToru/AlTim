from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SimpleUser, Flight, Review
from django.shortcuts import render, redirect, render_to_response
from django.middleware.csrf import CsrfViewMiddleware

class UserRegistrationForm(UserCreationForm):
    first_name               = forms.CharField(max_length=30)
    last_name                = forms.CharField(max_length=30)
    email                    = forms.EmailField()
    phone                    = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = SimpleUser
        fields = ('username', 'first_name', 'last_name','phone', 'email',)

class FlightFindByID(forms.ModelForm):
    flight_name              = forms.CharField(max_length=30)
    class Meta:
        model = Flight
        fields = ('flight_name',)

class UserSettingsForm(forms.ModelForm):
    first_name               = forms.CharField(max_length=30)
    last_name                = forms.CharField(max_length=30)
    email                    = forms.EmailField()
    phone                    = forms.CharField()
    date_of_birth            = forms.DateField()

    class Meta:
        model = SimpleUser
        fields = ('first_name', 'last_name','phone', 'email', 'date_of_birth',)

class UserImageForm(forms.ModelForm):
    userImg                 = forms.ImageField()

    class Meta:
        model = SimpleUser
        fields = ('userImg',)

class SimpleUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = SimpleUser
        fields = ('email','username', 'userImg')

class ReviewForm(forms.ModelForm):
    user                     = None
    plane                    = None
    review_text              = forms.CharField(widget=forms.Textarea)
    rating                   = forms.FloatField()
    class Meta:
        model = Review
        fields = ('review_text','rating')
