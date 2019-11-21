from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings

class Ticket(models.Model):
    is_two_flight=models.BooleanField(default=0)
    ticket_buy_date=models.DateTimeField('Date when flight was bought',default=0)


class Flight(models.Model):
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE, default='NULL')
    flight_name=models.CharField('name of flight',max_length=20)
    flight_initial_date=models.DateTimeField('date of departure')
    flight_last_date=models.DateTimeField('date of arrival')
    flight_initial_place=models.CharField('place of departure',max_length=50)
    flight_last_place=models.CharField('place of arrival',max_length=50)
    flight_rating=models.FloatField('rating of flight',default=0.0)
    flight_price=models.IntegerField('price of flight',default=0)
    plane_name=models.CharField('name of plane',max_length=20,default='NULL')
    flight_aircompany=models.ImageField( upload_to='user_avas/', default='NULL')

    def __str__(self):
        return self.flight_name

class SimpleUser(AbstractUser):
	userImg = models.ImageField(upload_to='user_avas/', default='NULL')

	def __str__(self):
		return self.username


class Review(models.Model):
    flight=models.ForeignKey(Flight, on_delete=models.CASCADE)
    review_text=models.TextField('text of review')
    review_rating=models.FloatField('rating of review')
    review_date=models.DateTimeField('date of review')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
