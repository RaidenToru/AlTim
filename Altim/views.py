from django.shortcuts import render, redirect
from .models import *
from Altim.forms import *
from django.views.generic.edit import CreateView, UpdateView, View
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from Altim.models import SimpleUser
from django.contrib.auth.decorators import login_required

#Main page
def index(request):
    cities = City.objects.all()
    return render(request,'index.html',{'cities':cities})

def search(request):
    cities = City.objects.all()
    try:
        if request.method=="POST":
            fromq = request.POST.get('from')
            whereq = request.POST.get('where')
            checkin= request.POST.get('checkin')
            checkout = request.POST.get('checkout')
            default_date='2000-01-01'
            flights_template = Flight.objects.filter(flight_initial_place=City.objects.get(city_name__icontains=fromq), flight_last_place=City.objects.get(city_name__icontains=whereq))

            return render(request, 'search.html',{'flights':flights_template,'cities':cities})
    except:
        return render(request,'search.html',{'cities':cities,'empty':"no one"})


#Personal user page
def personal(request, user_id):
    tickets = Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
    flights = Flight.objects.filter(user=SimpleUser.objects.get(pk=user_id))
    return render(request, 'personalPage.html',{'tickets':tickets, 'flights':flights})


#User's flight search results
def personalSearch(request,user_id):
    try:
        if request.method=="POST":
            query = request.POST.get('q')
            flights_result = Flight.objects.filter(flight_name__icontains=query, user=SimpleUser.objects.get(pk=user_id))
            tickets = Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
            flights = Flight.objects.filter(user=SimpleUser.objects.get(pk=user_id))
            return render(request,'personalSearch.html',{'flights_result':flights_result,'tickets':tickets, 'flights':flights})
    except:
        return render(request,'personalSearch.html')


#User's profile settings
@login_required
def settings(request):
    if request.method == "POST":
        u_form = UserSettingsForm(request.POST, instance=request.user)
        i_form = UserImageForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and i_form.is_valid():
            u_form.save()
            i_form.save()
            return redirect('/personal/'+str(request.user.id))
    else:
        u_form = UserSettingsForm(instance=request.user)
        i_form = UserImageForm(instance=request.user)
    context = {
        'u_form':u_form,
        'i_form':i_form
    }
    return render(request, 'settings.html', context)


#Page, where presents map with flights
def map(request):
    return render(request,'map.html')

def mapResult(request):
    if request.method=="POST":
        try:
            flight_name = request.POST.get('id')
            flight = Flight.objects.get(flight_name=flight_name)
            return render(request,'mapResults.html',{'flight':flight})
        except:
            return render(request,'mapResults.html')
    return render(request,'mapResults.html')


#sign in/up, log out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

class registerView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
