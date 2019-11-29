from django.shortcuts import render, redirect
from .models import Ticket,Flight,SimpleUser
from Altim.forms import UserRegistrationForm
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from Altim.models import SimpleUser

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def index(request):
    return render(request,'index.html')

def personal(request):
    user_id=1
    tickets=Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
    flights=Flight.objects.filter(user=SimpleUser.objects.get(pk=user_id))

    return render(request, 'personalPage.html',{'tickets':tickets, 'flights':flights})

def map(request):
    return render(request, 'map.html')

def user(request):
    b = SimpleUserChangeForm(username='Timka')
    return b.objects

class registerView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
