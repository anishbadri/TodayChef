from flask import Flask, request, redirect
import Info_File
import main
# , Anish, RemainderSend
from main import Remainder
from twilio import twiml


app = Flask(__name__)


@app.route("/", methods=['GET','POST'])

def index():
	return 'This is a very simple sms notification for TodayChef'

@app.route("/sms", methods=['GET','POST'])	
def sms_reply():
	#Read incoming message
	IncomingMsg = request.values.get('Body',None)
	MessageFrom = request.values.get('From')

	resp = twiml.Response()

	#check for the message from my roomates

	# print (MessageFrom)
	# main.SendMessage(MessageFrom,"FirstReply")
	if MessageFrom in Info_File.Roomates:
		if IncomingMsg == "Yes":
			main.Remainder(Info_File.Roomates[MessageFrom]+ "    Is cooking today")
		elif IncomingMsg == "No":
			main.Remainder(Info_File.Roomates[MessageFrom]+ "    Is not cooking today, If you are going to cook reply Yes or No?")
		else :	
			main.RemainderSend(MessageFrom,Info_File.WrongReply)
	# if "Anish" == Numbers[MessageFrom] :

	#    resp.message("its "+Numbers[MessageFrom] )
	else :
	   resp.message("You are foolish, Don't undermine TodayChef developer")

	return str(resp)


if __name__ == "__main__":
	app.run(debug=True)

	
