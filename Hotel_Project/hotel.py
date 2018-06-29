# -*- coding: utf-8 -*-
# “””
# hotel.py
# This is the Hotel class file 
# “””    


class Hotel(): 
    hotels = []
    def __init__(self, number,hotel_name, city,total_rooms,empty_rooms):
        self.number = number
        self.hotel_name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

        Hotel.hotels.append([self.number , self.hotel_name, self.city, self.total_rooms, 
        self.empty_rooms])

    def list_hotels_in_city(self, city):
        for hotel in Hotel.hotels:
            if hotels[hotels.index(hotel)][2] == city:
                print "Hotel Name : "+hotels[hotels.index(hotel)][1]+" /n Total of rooms : "+hotels[hotels.index(hotel)][3]

   