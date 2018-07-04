# -*- coding: utf-8 -*-
####################################
#customer.py                       #
#this is the customer class file   #
####################################


class Customer():
    customers = []
    def __init__(self,number,customer_name):
        self.number = number
        self.customer_name = customer_name

        Customer.customers.append([self.number,self.customer_name])
        print 'we added a customer with these information : '+'N:'+number +' Name : '+ customer_name
    
    @classmethod
    def list_customers(self):
        i = 1
        for customer in self.customers:
            print "Customer N"+str(i)+": "+str(customer)
            i+=1
