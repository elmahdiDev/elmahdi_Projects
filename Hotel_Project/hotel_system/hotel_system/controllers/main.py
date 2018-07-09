# -*- coding: utf-8 -*-
##################################
#      main.py                   #
#      this is the main file     #
##################################

from hotel import Hotel
from reservation import Reservation
from notification import Notification
from customer import Customer
from django.http import HttpResponse


def add_hotel(number,name,city,total_rooms,empty_rooms):
    h=Hotel(number,name,city,total_rooms,empty_rooms)
    print 'we added these hotels informations : '+ h.hotel_name+'////'+h.city+'////'+str(h.total_rooms)+'////'+str(h.empty_rooms)

def check_and_reserve_room(hotel_name,customer,check_in,check_out):
    Reservation(hotel_name,customer,check_in,check_out)
     

def check_hotel_reservations(hotel_name):
    Reservation.list_reservations_for_hotel(hotel_name)

def send_sms(number,message):
    Notification(number,message)

def add_customer(number,customer_name):
    Customer(number,customer_name)

def list_all_customers(request):
    customers_list_output= '<ul style="width:auto;height:auto;background-color:lightgrey;borber-radius:6px;font-size:20px;padding:30px;">'
    for c in Customer.customers:
        customers_list_output += "<li>"+str(Customer.customers[Customer.customers.index(c)][1])+"</li>"
    customers_list_output += "</ul>"
    return HttpResponse(customers_list_output)

def list_all_hotels(request):
    hotels_list_output= '<ul style="width:auto;height:auto;background-color:lightgrey;borber-radius:6px;font-size:20px;padding:30px;">'
    for h in Hotel.hotels:
        hotels_list_output += "<li>"+str(Hotel.hotels[Hotel.hotels.index(h)][1])+"</li>"
    hotels_list_output += "</ul>"
    return HttpResponse(hotels_list_output)

def list_hotel_in_city(request):
    hotels_list_output= '<ul style="width:auto;height:auto;background-color:lightgrey;borber-radius:6px;font-size:20px;padding:30px;">'
    for h in Hotel.hotels:
        if Hotel.hotels[Hotel.hotels.index(h)][2]=="city":
            hotels_list_output += "<li>"+str(Hotel.hotels[Hotel.hotels.index(h)][1])+"</li>"
    hotels_list_output += "</ul>"
    return HttpResponse(hotels_list_output)

def list_hotel_reservations(request):
    reservations_list_output= '<ul style="width:auto;height:auto;background-color:lightgrey;borber-radius:6px;font-size:20px;padding:30px;">'
    reservations_list_output += "<li style='font-size:30px'>"+"Figuig Reservations"+"</li>"
    for reserve_info in Reservation.reservations:
        if Reservation.reservations[Reservation.reservations.index(reserve_info)][0] == 'figuig':
            reservations_list_output += "<li>"+str(Reservation.reservations[Reservation.reservations.index(reserve_info)])+"</li>"
    reservations_list_output += "</ul>"
    return HttpResponse(reservations_list_output)

    