from django.shortcuts import render, redirect
from .models import Ticket,Flight,SimpleUser
from Altim.forms import UserRegistrationForm, UserSettingsForm, FlightFindByID, UserImageForm
from django.views.generic.edit import CreateView, UpdateView, View
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from Altim.models import SimpleUser
from django.contrib.auth.decorators import login_required

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
    return render(request,'map.html')

def mapResult(request):
    if request.method=="POST":
        try:
            flight_name=request.POST.get('id')
            flight=Flight.objects.get(flight_name=flight_name)
            return render(request,'mapResults.html',{'flight':flight})
        except:
            return render(request,'mapResults.html')
    return render(request,'mapResults.html')

class registerView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

@login_required
def settingsView(request):
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

def get_search_result(request, user_id):
    try:
        if request.method=="POST":
            query=request.POST.get('q')
            flights_result=Flight.objects.filter(flight_name__icontains=query, user=SimpleUser.objects.get(pk=user_id))
            tickets=Ticket.objects.filter(user=SimpleUser.objects.get(pk=user_id))
            return render(request,'personalSearch.html',{'flights_result':flights_result,'tickets':tickets})
    except:
        return render(request,'personalSearch.html')
