from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from datetime import datetime
from django.conf import settings

class Ticket(models.Model):
    ticket_name=models.CharField(max_length=20)
    is_two_flight=models.BooleanField()
    ticket_buy_date=models.DateTimeField('Date when flight was bought')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket_price=models.IntegerField('price of ticket',default=0)


class Flight(models.Model):
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight_name=models.CharField('name of flight',max_length=20)
    flight_initial_date=models.DateField('date of departure',null=True,blank=True)
    flight_last_date=models.DateField('date of arrival',null=True,blank=True)
    flight_initial_time=models.TimeField('time of departure',null=True,blank=True)
    flight_last_time=models.TimeField('time of arrival',null=True,blank=True)
    flight_initial_place=models.CharField('place of departure',max_length=50)
    flight_last_place=models.CharField('place of arrival',max_length=50)
    flight_rating=models.FloatField('rating of flight')
    plane_name=models.CharField('name of plane',max_length=20)
    flight_aircompany=models.ImageField( upload_to='user_avas/')
    aircompany_name=models.CharField(max_length=20)
    flight_time=models.CharField(max_length=20)

    def __str__(self):
        return self.flight_name

class SimpleUser(AbstractUser):
    userImg = models.ImageField(upload_to='user_avas/')
    phone=models.CharField('Phone of user',max_length=20)
    date_of_birth=models.DateField('date of birth',auto_now=False, auto_now_add=False,null=True,blank=True)
    group = Group()
    user_permissions=Permission()

    def __str__(self):
        return self.username


class Review(models.Model):
    flight=models.ForeignKey(Flight, on_delete=models.CASCADE)
    review_text=models.TextField('text of review')
    review_rating=models.FloatField('rating of review')
    review_date=models.DateTimeField('date of review')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
