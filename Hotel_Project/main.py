# -*- coding: utf-8 -*-
##################################
#      main.py                   #
#      this is the main file     #
##################################

from hotel import Hotel
from reservation import Reservation
from notification import Notification
from customer import Customer


def add_hotel(number,name,city,total_rooms,empty_rooms):
    hotel_name = name
    hotel_name = Hotel(number,name,city,total_rooms,empty_rooms)
    print 'we added these hotels informations : '+ str(Hotel.hotels)

def check_and_reserve_room(hotel_name,customer,check_in,check_out):
	Reservation(hotel_name,customer,check_in,check_out)

def check_hotel_reservations(hotel_name):
	Reservation.list_reservations_for_hotel(hotel_name)

def send_sms(number,message):
	Notification(number,message)

def add_customer(number,customer_name):
	Customer(number,customer_name)

def list_all_customers():
	Customer.list_customers()

