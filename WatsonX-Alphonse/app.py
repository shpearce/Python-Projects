from flask import Flask, request
import requests

'''
app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def webhook():
	
	if request.method == "GET":
		return 'Hello World'
	
	elif request.method == "POST":
		payload = request.json
		return "Message received"
	
	else:
		print(request.data)

if __name__ == "__main__":
    app.run(debug=True)
'''

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Get JSON data from the POST request
    
    # Process the data or perform actions based on the webhook payload
    # For demonstration purposes, let's just print the received data
    print("Received data:", data)

    return '', 200  # Return an empty response with HTTP status code 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)