from flask import Flask, request, redirect
from Info_File import Numbers
from main import SendMessage, Anish
from main import Remainder
from twilio import twiml
import datetime
import schedule


print (datetime.datetime.now())
app = Flask(__name__)
# schedule.every(1).minutes.do(Remainder)
@app.route("/sms", methods=['GET','POST'])
def sms_reply():
	IncomingMsg = request.values.get('Body',None)
	MessageFrom = request.values.get('From')

	resp = twiml.Response()
	# resp.message("Mesage received by Anish")

	print (MessageFrom)
	SendMessage(MessageFrom,"FirstReply")

	if "Anish" == Numbers[MessageFrom] :
	   resp.message("its "+Numbers[MessageFrom] )
	else :
	   resp.message("You are foolish")

	return str(resp)
	print("Hello")




# while True:
# 	schedule.run_pending()
if __name__ == "__main__":
	app.run(debug=True)
	
