# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import *

def AllHotels(request):
    # allhotels = '<ul style="width:auto;height:auto;background-color:lightgrey;borber-radius:6px;font-size:20px;padding:30px;">'
    # for hotel in Hotel.objects.all():
    #     allhotels += '<li>'+hotel.hotel_name+'</li>'
    # allhotels += '</ul>'
    # return HttpResponse(allhotels)
    return render(request,"reservation/hotels.html",{"hotels":Hotel.objects.all()})


# def HotelInCity(request):
#     hotelincity = '<ul style="width:auto;height:auto;background-color:lightgrey;borber-radius:6px;font-size:20px;padding:30px;">'
#     for hotel in Hotel.objects.all():
#         if hotel.hotel_city == 'casa':
#             hotelincity += '<li>'+hotel.hotel_name+'</li>'
#     hotelincity += "</ul>"
#     return HttpResponse(hotelincity)

def AllCustomers(request):
    return render(request,"reservation/customers.html",{'customers':Customer.objects.all()})

def AllReservations(request):
    # reservationlist = '<ul style="width:auto;height:auto;background-color:lightgrey;borber-radius:6px;font-size:20px;padding:30px;">'
    # for r in Reservation.objects.all():
    #     reservationlist += '<li>'+'The Customer : '+str(r.customer)+' Reserved on : '+str(r.hotel)+'</li>'
    # reservationlist += '</ul>'
    # return HttpResponse(reservationlist)
    return render(request,"reservation/reservations.html",{'reservations':Reservation.objects.all()})
