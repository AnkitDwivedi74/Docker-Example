from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/receive_message', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        return jsonify({'received_data': data})
    else:
        return render_template('received_message.html', received_message="No message received.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

