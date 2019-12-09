from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, View
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from Altim.models import SimpleUser
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
            checkin = request.POST.get('checkin')
            checkout = request.POST.get('checkout')
            is_two_flight=False
            if checkout!='':
                is_two_flight=True
            print(checkout)
            flights_checkin = Flight.objects.filter(flight_initial_place=City.objects.get(city_name__icontains=fromq), flight_last_place=City.objects.get(city_name__icontains=whereq),flight_initial_date__icontains=checkin,user=None)
            flights_checkout = Flight.objects.filter(flight_initial_place=City.objects.get(city_name__icontains=whereq), flight_last_place=City.objects.get(city_name__icontains=fromq),flight_initial_date__icontains=checkout,user=None)
            return render(request, 'search.html',{'flights_checkin':flights_checkin,'cities':cities,'flights_checkout':flights_checkout,'is_two_flight':is_two_flight})
    except:
        return render(request,'search.html',{'cities':cities,'empty':"no one"})


#Operation to create ticket for user
def boughtinout(request):
    try:
        if request.method=="POST":
            user_id = request.POST.get('user_id')
            flightin_id = request.POST.get('flightin_id')
            flightout_id = request.POST.get('flightout_id')
            flightin = Flight.objects.get(pk=flightin_id)
            flightout = Flight.objects.get(pk=flightout_id)
            ticket = Ticket(
                    is_two_flight            = True,
                    user                     = SimpleUser.objects.get(pk=user_id),
                    ticket_price             = flightin.flight_price+flightout.flight_price,
                    ticket_buy_date          = timezone.now())
            ticket.save()
            flightin_user = Flight(
                    ticket                   = ticket,
                    user                     = SimpleUser.objects.get(pk=user_id),
                    flight_initial_place     = flightin.flight_initial_place,
                    flight_last_place        = flightin.flight_last_place,
                    plane                    = flightin.plane,
                    aircompany               = flightin.aircompany,
                    flight_name              = flightin.flight_name,
                    flight_initial_date      = flightin.flight_initial_date,
                    flight_last_date         = flightin.flight_last_date,
                    flight_initial_time      = flightin.flight_initial_time,
                    flight_last_time         = flightin.flight_last_time,
                    flight_rating            = flightin.flight_rating,
                    flight_time              = flightin.flight_time,
                    flight_price             = flightin.flight_price)
            flightin_user.save()
            flightout_user = Flight(
                    ticket                   = ticket,
                    user                     = SimpleUser.objects.get(pk=user_id),
                    flight_initial_place     = flightout.flight_initial_place,
                    flight_last_place        = flightout.flight_last_place,
                    plane                    = flightout.plane,
                    aircompany               = flightout.aircompany,
                    flight_name              = flightout.flight_name,
                    flight_initial_date      = flightout.flight_initial_date,
                    flight_last_date         = flightout.flight_last_date,
                    flight_initial_time      = flightout.flight_initial_time,
                    flight_last_time         = flightout.flight_last_time,
                    flight_rating            = flightout.flight_rating,
                    flight_time              = flightout.flight_time,
                    flight_price             = flightout.flight_price)
            flightout_user.save()
            return render(request,'bought.html',{'success':"Thank you for your purchase"})
    except:
        return render(request,'bought.html',{'fail':"Error"})

def boughtin(request):
    try:
        user_id = request.POST.get('user_id')
        flightin_id = request.POST.get('flightin_id')
        flightin = Flight.objects.get(pk=flightin_id)
        ticket = Ticket(
                is_two_flight            = False,
                user                     = SimpleUser.objects.get(pk=user_id),
                ticket_price             = flightin.flight_price,
                ticket_buy_date          = timezone.now())
        ticket.save()
        flightin_user = Flight(
                ticket                   = ticket,
                user                     = SimpleUser.objects.get(pk=user_id),
                flight_initial_place     = flightin.flight_initial_place,
                flight_last_place        = flightin.flight_last_place,
                plane                    = flightin.plane,
                aircompany               = flightin.aircompany,
                flight_name              = flightin.flight_name,
                flight_initial_date      = flightin.flight_initial_date,
                flight_last_date         = flightin.flight_last_date,
                flight_initial_time      = flightin.flight_initial_time,
                flight_last_time         = flightin.flight_last_time,
                flight_rating            = flightin.flight_rating,
                flight_time              = flightin.flight_time,
                flight_price             = flightin.flight_price)
        flightin_user.save()
        return render(request,'bought.html',{'success':"Thank you for your purchase"})
    except:
        return render(request,'bought.html',{'fail':"Error"})


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
