# -*- coding: utf-8 -*-
##################################
#      main.py                   #
#      this is the main file     #
##################################

from hotel import Hotel


def start_app():
    rotana_hotel = Hotel(20,'Rotana','Abu Dhabi',200,40)
    sheraton_hotel = Hotel(21,'Sheraton','Abu Dhabi',300,100)
    print Hotel.hotels
start_app()
