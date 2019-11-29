from django.shortcuts import render, redirect
from .models import Ticket,Flight
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
    latest_flight_list=Ticket.objects.order_by('-ticket_buy_date')
    return render(request, 'personalPage.html',{'latest_flight_list':latest_flight_list})

def map(request):
    return render(request, 'map.html')

def user(request):
    b = SimpleUserChangeForm(username='Timka')
    return b.objects

class registerView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
