# -*- coding: utf-8 -*- 

########
#     notification.py
#     this is the notification class file
########
from twilio.rest import Client

class Notification():
	def __inti__(self,number,message):
		self.number = number
		self.message = message
		# Your Account SID from twilio.com/console
		account_sid = "ACd4029af67b7ed2c9054b626adc9c3de6"
		# Your Auth Token from twilio.com/console
		auth_token  = "token"

		client = Client(account_sid, auth_token)

		message = client.messages.create(
	    	to= "+"+str(number), 
	    	from_="+12692154193",
	    	body= message)

		return "message succesfully sended"