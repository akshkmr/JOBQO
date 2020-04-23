
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from recipes import *
from message import *

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def reply_with_recipe_info():
	rcvd_msg = request.values.get('Body')
	responded = False
	resp = MessagingResponse()
	# msg = resp.message()
	print('Message sent', rcvd_msg)

	if 'Hi' in rcvd_msg or 'Hey' in rcvd_msg or 'hey' in rcvd_msg or 'hi' in rcvd_msg or 'Hii' in rcvd_msg or 'hii' in rcvd_msg or 'update' in rcvd_msg or 'Update' in rcvd_msg:
		text = f'Hey, I am Jobqo 👋, \n\n Please choose a profile you interested in 👇 \n *A*. Software Developer\n *B*. Data Engineer/Data Analyst \n *C*. Business Analyst'
		resp.message(text)
		responded = True

	if rcvd_msg == 'A' or rcvd_msg == 'a':
		recipes = search_recipe("Software")
		message = convert_result_to_message(recipes)
		for msg in message:
			resp.message(msg)
			print(msg)
		responded = True	
	
	if rcvd_msg == 'B' or rcvd_msg == 'b':
		recipes = search_recipe("Data")
		message = convert_result_to_message(recipes)
		for msg in message:
			resp.message(msg)
			print(msg)
		responded = True

	if rcvd_msg == 'C' or rcvd_msg == 'c':
		recipes = search_recipe("Business")
		message = convert_result_to_message(recipes)
		for msg in message:
			resp.message(msg)
			print(msg)
		responded = True

	if "Thanks" in rcvd_msg or "thanks" in rcvd_msg or "thnks" in rcvd_msg:
		resp.message("The pleasure was all mine 😊")
		responded = True

	if responded == False:
		resp.message("😞")
		resp.message('Sorry, I can only update you about job opportunities')
		print("Unknown Keyword")
		
	return str(resp)


if __name__ == '__main__':
	app.run()