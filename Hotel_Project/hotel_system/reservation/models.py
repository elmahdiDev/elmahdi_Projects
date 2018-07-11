# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    hotel_city = models.CharField(max_length=50)
    total_rooms = models.IntegerField()
    empty_rooms = models.IntegerField()

    def __str__(self):
        return self.hotel_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_number = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name

class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel)
    customer = models.ForeignKey(Customer)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return  self.customer.customer_name +"---Reserver on --->"+self.hotel.hotel_name 
