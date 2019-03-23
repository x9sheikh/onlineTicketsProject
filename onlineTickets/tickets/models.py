from django.db import models

# Create your models here.
class Ticket(models.Model):
    name                = models.CharField(max_length=64)
    superClassSeat      = models.BooleanField(default=False)
    student             = models.BooleanField(default=False)
    seatNo              = models.CharField(max_length=5)
    movieTitle          = models.CharField(max_length=64)
    ticketCreateTime    = models.DateTimeField(auto_now_add=True)