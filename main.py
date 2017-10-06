from twilio.rest import TwilioRestClient as Client
from Info_File import Accountsid, AAuthId, ANNum, TwilioNum

print(Accountsid)

client = Client(Accountsid,AAuthId)	

client.messages.create(to=ANNum,from_=TwilioNum,body="First message from python to Anish for ChefTurn")	 	
# print("Success");