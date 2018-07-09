# -*- coding: utf-8 -*-
from hotel import Hotel
from customer import Customer

class Reservation():
    reservations = []
    def __init__ (self,hotel_name, customer_name,check_in,check_out):
        self.hotel_name = hotel_name
        self.customer_name = customer_name
        self.check_in = check_in
        self.check_out = check_out
        torf = False
        for h in Hotel.hotels:
            if Hotel.hotels[Hotel.hotels.index(h)][1]==hotel_name:
                if Hotel.hotels[Hotel.hotels.index(h)][-1]>0:
                    Hotel.hotels[Hotel.hotels.index(h)][-1]=(Hotel.hotels[Hotel.hotels.index(h)][-1])-1
                    self.add_new_reservation(self.hotel_name,self.customer_name,self.check_in,self.check_out)
                else:
                    print "No rooms available on the hotel : "+hotel_name
        if torf == True:    
            print "there is not a hotel with the name :"+hotel_name
    
   
    def add_new_reservation(self,hotel_name, customer_name,check_in,check_out):
        i = 0
        succed = False
        while i < len(Customer.customers): 
            if Customer.customers[i][1] == customer_name:
                self.reservations.append([self.hotel_name,self.customer_name,self.check_in,self.check_out])
                print "reservation success !You reserved a room on the hotel : "+hotel_name
                succed = True
            i += 1
        if succed == False:
            print "You are not registred! Please register before you reserve !"

    
    @classmethod
    def list_reservations_for_hotel(self,hotel_name):
        for reserve_info in self.reservations:
            if self.reservations[self.reservations.index(reserve_info)][0] == hotel_name:
                print 'Costumer name : '+str(self.reservations[self.reservations.index(reserve_info)][1])+' <<<|>>> Hotel name : '+str(self.reservations[self.reservations.index(reserve_info)][0])+" <<<|>>>  from : "+str(self.reservations[self.reservations.index(reserve_info)][2]) +" To : "+str(self.reservations[self.reservations.index(reserve_info)][3])




        



