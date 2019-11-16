from django.db import models

class Flight(models.Model):
    flight_name=models.CharField('name of flight',max_length=20)
    flight_aircompany=models.CharField('path to image of aircompany', max_length=100)
    flight_initial_date=models.DateTimeField('date of departure')
    flight_last_date=models.DateTimeField('date of arrival')
    flight_initial_place=models.CharField('place of departure',max_length=50)
    flight_last_place=models.CharField('place of arrival',max_length=50)
    flight_rating=models.FloatField('rating of flight')

    def __str__(self):
        return self.flight_name

class Review(models.Model):
    flight=models.ForeignKey(Flight, on_delete=models.CASCADE)
    review_text=models.TextField('text of review')
    review_rating=models.FloatField('rating of review')
    review_date=models.DateTimeField('date of review')
