from twilio.rest import TwilioRestClient as Client
from Info_File import Accountsid, AAuthId, ANNum, TwilioNum, Anish
print(Accountsid)

def SendMessage(number,message):
	client = Client(Accountsid,AAuthId)	
	client.messages.create(to=number,from_=TwilioNum,body=message)	

def ReminderSend(number, message):
	client = Client(Accountsid,AAuthId)	
	client.messages.create(to=number,from_=TwilioNum,body=message)	

def Remainder():
	print(Anish)
	print("Running timer")

 	


# print("Success");