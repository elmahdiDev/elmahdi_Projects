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