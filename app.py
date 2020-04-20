from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

@app.route("/sms", methods=['POST'])
def reply():
   
	incoming_msg = request.values.get('Body', '')
	#print(incoming_msg)
	resp = MessagingResponse()
	msg = resp.message()
	responded = False

	if 'Hi' in incoming_msg or 'Hey' in incoming_msg:
		text = f'Hey 👋, \nThis is a Covid-Bot developed by Akshay to provide latest information updates i.e cases in different countries and create awareness to help you and your family stay safe. \n Please enter one of the following option 👇 \n *A*. Covid-19 statistics *Worldwide*. \n *B*. Covid-19 cases in *India*. \n *C*. Covid-19 cases in *China*. \n *D*. Covid-19 cases in *USA*. \n *E*. Coronavirus cases in *Italy*. \n *F*. How does it *Spread*? \n *G*. *Preventive measures* to be taken.'
		msg.body(text)
		responded = True

	return str(resp)
if __name__ == "__main__":
	app.run(debug=True)
