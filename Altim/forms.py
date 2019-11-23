from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SimpleUser

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.IntegerField()
    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = SimpleUser
        fields = ('username', 'first_name', 'last_name','phone', 'email', 'password',)


class SimpleUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = SimpleUser
        fields = ('email','username', 'userImg')
