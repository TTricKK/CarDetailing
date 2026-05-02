from django.db import models

# Create your models here.


"""
TABLE BOOKING_INFO

Name = CharField
REGO = CharField
Car = Charfield
Size = Choices(Small, Medium, Large)
Date = DateField
Time = Time selection dropdown 30 minute intervals
Price = Auto Loaded based off of service selected
Duration = Auto Loaded based off of service selected

TABLE SERVICE_OPTIONS
SERVICE = Choices(Exterior, Interior, Interior and Exterior, Deluxe)

Exterior = Pricing, Duration
Interior = Pricing, Duration
Interior and Exterior = Pricing, Duration
Deluxe = Pricing, Duration


"""

class Service(models.Model):
    SERVICE_CHOICES = [
        ('exterior', 'Exterior')
        ('interior', 'Interior')
        ('interior_exterior', 'Interior & Exterior')
        ('deluxe', 'Deluxe')
    ]
    service_type = models.CharField(max_length = 50, choices = SERVICE_CHOICES)
    price = models.DecimalField(max_digits = 6, decimal_place = 2)
    duration_minutes = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name

class Booking(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small')
        ('medium', 'Medium')
        ('large', 'Large')
    ]
    name = models.Charfield(max_length = 100)
    rego =  models.Charfield(max_length = 10)
    car = models.Charfield(max_length = 100)
    size = models.CharField(max_length = 10, choices = SIZE_CHOICES)
    service = models.ForeignKey(Service, on_delete = models.PROTECT)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add = True)
