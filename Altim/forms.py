from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SimpleUser
from django.shortcuts import render, redirect, render_to_response
from django.middleware.csrf import CsrfViewMiddleware

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField()
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = SimpleUser
        fields = ('username', 'first_name', 'last_name','phone', 'email',)

class UserSettingsForm(UserChangeForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField()
    date_of_birth = forms.DateField()
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta(UserChangeForm.Meta):
        model = SimpleUser
        fields = ('first_name', 'last_name','phone', 'email', 'date_of_birth')

def settings(request):
    form = SimpleUserChangeForm
    if request.method == 'POST':
        form = SimpleUserChangeForm(request)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            date_of_birth = form.cleaned_data['date_of_birth']
            if(user is not None):
                if(first_name is not None):request.user.first_name = first_name
                if(last_name is not None):request.user.last_name = last_name
                if(email is not None):request.user.email = email
                if(phone is not None):request.user.phone = phone
                if(date_of_birth is not None):request.user.date_of_birth = date_of_birth
                return redirect('/personal')
    c = {}
    return render_to_response("settings.html", c)

class SimpleUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = SimpleUser
        fields = ('email','username', 'userImg')
