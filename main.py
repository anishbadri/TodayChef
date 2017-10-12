from twilio.rest import TwilioRestClient as Client
from Info_File import Accountsid, AAuthId, TwilioNum
import Info_File 
print(Accountsid)

# def SendMessage(number,message):
# 	client = Client(Accountsid,AAuthId)	
# 	client.messages.create(to=number,from_=TwilioNum,body=message)	

def RemainderSend(number, message):
	client = Client(Accountsid,AAuthId)	
	client.messages.create(to=number,from_=TwilioNum,body="--TodayChef--"+message)	

def Remainder(message):
	for mate in Info_File.Roomates:
		# msgbody = Info_File.Roomates[mate]+ "   " + message
		msgbody = message
		print (msgbody)
		RemainderSend(mate,msgbody)


# if __name__ == '__main__':
# 	Remainder("Are you cooking today? Reply 'Yes' or 'No' ")


 	


# print("Success");