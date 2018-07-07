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

def execute():
    #add customer
    print '#add customer'
    main.add_customer('+25555555','meryem')
    main.add_customer('+2555545','elmahdi')
    main.add_customer('+25444455','yassin')



    #adding hotel
    print '#adding hotel'
    main.add_hotel(88,'figuig','oujda',200,10)
    main.add_hotel(88,'oujda','oujda',200,10)
    main.add_hotel(88,'casa','oujda',200,10)



    print '#check if there is free rooms to reserve if ther is free rooms it will reserve a room automaticlly '
    main.check_and_reserve_room('figuig','elmahdi','2/5/17','2/5/17')
    main.check_and_reserve_room('oujda','meryem','2/5/17','2/5/17')
    main.check_and_reserve_room('casa','yassin','2/5/17','2/5/17')
    main.check_and_reserve_room('figuig','omar','2/5/17','2/5/17')





