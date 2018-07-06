# -*- coding: utf-8 -*-
#################################################
#         tester.py                             #
#         this is the tester file               #
#################################################

import main
from customer import Customer
from reservation import Reservation
from notification import Notification
from hotel import Hotel

#add customer
print '#add customer'
main.add_customer('+25555555','dddfff')
main.add_customer('+2555545','elmahdi')
main.add_customer('+25444455','dddf')

print "<<--------------------------------------->>" 

#list all customers
print'#list all customers'
main.list_all_customers()

print "<<--------------------------------------->>" 

#adding hotel
print '#adding hotel'
main.add_hotel(88,'figuig','oujda',200,10)

print '<<--------------------------------------->> '

#check if there is free rooms to reserve if there is free rooms it will reserve a room automaticlly 
print '#check if there is free rooms to reserve if ther is free rooms it will reserve a room automaticlly '
main.check_and_reserve_room('figuig','elmahdi','2/5/17','2/5/17')
main.check_and_reserve_room('oujda','meryem','2/5/17','2/5/17')
main.check_and_reserve_room('figuig','yassin','2/5/17','2/5/17')
main.check_and_reserve_room('figuig','omar','2/5/17','2/5/17')

print '<<--------------------------------------->> '

#prints names of people who reserve rooms and the hotel name
print '#prints names of people who reserve rooms and the hotel name'
main.check_hotel_reservations('figuig')

print '<<--------------------------------------->> '

#send phone message 
print '#send phone message '
#main.send_sms('+212618738321','hello there')

print "<<--------------------------------------->>" 

