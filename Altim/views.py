from django.shortcuts import render, redirect
from .models import Ticket,Flight,SimpleUser
from Altim.forms import UserRegistrationForm

def index(request):
    return render(request,'index.html')

def personal(request):
    user_id=1
    tickets=Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
    flights=Flight.objects.filter(user=SimpleUser.objects.get(pk=user_id))

    return render(request, 'personalPage.html',{'tickets':tickets, 'flights':flights})

def map(request):
    return render(request, 'map.html')
