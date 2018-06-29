# -*- coding: utf-8 -*-
from hotel import Hotel

class Reservation():
    reservations = [['fff','cos']]
    def __init__ (self,hotel_name, customer_name):
        self.hotel_name = hotel_name
        self.customer_name = customer_name

        for hotels in Hotel.hotels:
            if Hotel.hotels[Hotel.hotels.index(hotels)][1]==hotel_name:
                if Hotel.hotels[Hotel.hotels.index(hotels)][-1]>0:
                    Hotel.hotels[Hotel.hotels.index(hotels)][-1]=(Hotel.hotels[Hotel.hotels.index(hotels)][-1])-1
                    add_new_reservation(hotel_name,customer_name)
                else:
                    print "No rooms available on the hotel : "+hotel_name
        print "there is not hotel with the name :"+hotel_name
        
    def add_new_reservation(hotel_name, customer_name):
        reservations.append(hotel_name,customer_name)
        print "reservation success !"

    def list_resevrations_for_hotel(hotel_name):
        for reserve_info in reservations:
            if reservations[reservations.index(reserve_info)][0] == hotel_name:
                print reservations[reservations.index(reserve_info)][1]
                return reservations[reservations.index(reserve_info)][1]





        



