from django.shortcuts import render, redirect
from .models import Ticket,Flight
from Altim.forms import UserRegistrationForm

def index(request):
    return render(request,'index.html')

def personal(request):
    latest_flight_list=Ticket.objects.order_by('-ticket_buy_date')
    return render(request, 'personalPage.html',{'latest_flight_list':latest_flight_list})

def map(request):
    return render(request, 'map.html')
