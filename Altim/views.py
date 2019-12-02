from django.shortcuts import render, redirect
from .models import Ticket,Flight,SimpleUser
from Altim.forms import UserRegistrationForm


def index(request):
    return render(request,'index.html')

def personal(request, user_id):
    tickets=Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
    flights=Flight.objects.filter(user=SimpleUser.objects.get(pk=user_id))

    return render(request, 'personalPage.html',{'tickets':tickets, 'flights':flights})

def map(request):
    return render(request, 'map.html')

def get_search_result(request,user_id):
    try:
        if request.method=="POST":
            query=request.POST.get('q')
            flights_result=Flight.objects.filter(flight_name__icontains=query, user=SimpleUser.objects.get(pk=user_id))
            tickets=Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
            return render(request,'personalSearch.html',{'flights_result':flights_result,'tickets':tickets})
    except:
        return render(request,'personalSearch.html')
