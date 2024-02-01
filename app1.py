from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="Hello from App1!")

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form.get('message')
    if message:
        # Send the message to App2
        app2_url = 'http://192.18.0.3:5002/receive_message'
        requests.post(app2_url, json={'message': message})
        return render_template('index.html', message=f"Message sent to App2: {message}")
    else:
        return "Bad Request", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

