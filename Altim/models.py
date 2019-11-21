from django.db import models

class Ticket(models.Model):
    is_two_flight=models.BooleanField(default=0)
    ticket_buy_date=models.DateTimeField('Date when flight was bought',default=0)




class Review(models.Model):
    review_text=models.TextField('text of review')
    review_rating=models.FloatField('rating of review')
    review_date=models.DateTimeField('date of review')
