from django.shortcuts import render, redirect
from .models import Ticket,Flight,SimpleUser
from Altim.forms import UserRegistrationForm, UserSettingsForm, settings
from django.views.generic.edit import CreateView, UpdateView, View
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from Altim.models import SimpleUser

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def index(request):
    return render(request,'index.html')

def personal(request, user_id):
    tickets=Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
    flights=Flight.objects.filter(user=SimpleUser.objects.get(pk=user_id))

    return render(request, 'personalPage.html',{'tickets':tickets, 'flights':flights})

def map(request):
    return render(request, 'map.html')

class registerView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def settingsView(request):
    return settings(request)
    
def get_search_result(request,user_id):
    try:
        if request.method=="POST":
            query=request.POST.get('q')
            flights_result=Flight.objects.filter(flight_name__icontains=query, user=SimpleUser.objects.get(pk=user_id))
            tickets=Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
            return render(request,'personalSearch.html',{'flights_result':flights_result,'tickets':tickets})
    except:
        return render(request,'personalSearch.html')
