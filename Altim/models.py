from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from datetime import datetime
from django.conf import settings


class City(models.Model):
    city_name                =models.CharField(max_length=20)

    def __str__(self):
        return self.city_name


class AirCompany(models.Model):
    company_name             =models.CharField(max_length=20)
    company_logo             =models.ImageField( upload_to='logos/')

    def __str__(self):
        return self.company_name


class Plane(models.Model):
    plane_name               =models.CharField(max_length=20)

    def __str__(self):
        return self.plane_name


class Ticket(models.Model):
    is_two_flight            =models.BooleanField()
    ticket_buy_date          =models.DateTimeField('Date when flight was bought')
    user                     =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket_price             =models.IntegerField('price of ticket',default=0)

    def __str__(self):
        return self.user.username+"'s ticket"


class Flight(models.Model):
    ticket                   =models.ForeignKey(Ticket, on_delete=models.CASCADE,null=True,blank=True)
    user                     =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    flight_initial_place     =models.ForeignKey(City, on_delete=models.CASCADE,related_name='flight_initial_place')
    flight_last_place        =models.ForeignKey(City, on_delete=models.CASCADE,related_name='flight_last_place')
    plane                    =models.ForeignKey(Plane, on_delete=models.CASCADE)
    aircompany               =models.ForeignKey(AirCompany,on_delete=models.CASCADE)
    flight_name              =models.CharField('name of flight',max_length=20)
    flight_initial_date      =models.DateField('date of departure',null=True,blank=True)
    flight_last_date         =models.DateField('date of arrival',null=True,blank=True)
    flight_initial_time      =models.TimeField('time of departure',null=True,blank=True)
    flight_last_time         =models.TimeField('time of arrival',null=True,blank=True)
    flight_rating            =models.FloatField('rating of flight')
    flight_time              =models.CharField(max_length=20)
    flight_price             =models.IntegerField('price of flight')

    def __str__(self):
        if self.user:
            return self.flight_name+" "+self.user.username
        return self.flight_name


class SimpleUser(AbstractUser):
    userImg                  =models.ImageField(upload_to='user_avas/',default='/default/image_6.jpg')
    phone                    =models.CharField('Phone of user',max_length=20)
    date_of_birth            =models.DateField('date of birth',auto_now=False, auto_now_add=False,null=True,blank=True)
    group                    =Group()
    user_permissions         =Permission()

    def __str__(self):
        return self.username
