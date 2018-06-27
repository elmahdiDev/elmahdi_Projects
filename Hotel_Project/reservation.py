# -*- coding: utf-8 -*-

hotels_list=[]
customers_list=[]
reservation_list=[]






def add_hotel(number,hotel_name, city,total_rooms,empty_rooms):
    HL=[number,hotel_name,city,total_rooms,empty_rooms]
    hotels_list.append(HL)
    print 'added new hotel with these information : '+HL



def add_customer(customer_name):
    customers_list.append(customer_name)
    print 'added new customer with the name : '+ customer_name 



def reserve_room (hotel_name, customer_name):
    for hotels in hotels_list:
    	if hotels[1]==hotel_name:
    		return True
    		if hotels[-1]>0:
    			hotels[-1]=hotels[-1]-1
    			return True,customer_name
    		else:
    			return False
    	else:
    		print "there is not hotel with the name :"+hotel_name




def add_new_reservation(hotel_name, customer_name):
    if reserve_room(hotel_name, customer_name) == True:
    	if reserve_room(hotel_name, customer_name)[0] == True:
    		reservation_list.append(hotel_name,customer_name)
    		print "reservation success !"
    	else:
    		print 'sorry no rooms available'
    else:
    	print 'sorry no rooms available'



def list_resevrations_for_hotel(hotel_name):
    for reserve_info in reservation_list:
    	if reserve_info[0] == hotel_name:
    		print reserve_info[1]



def list_hotels_in_city(city_name):
	for hotel in hotels_list:
		if hotel[2] == city_name:
			print "Hotel Name : "+hotel[1]+" Total of rooms : "+hotel[3]

	


