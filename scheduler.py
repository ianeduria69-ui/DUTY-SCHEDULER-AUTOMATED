from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

received_messages = []

# 1. Ruta para sa Home / Root (aron dili mo-gawas ang Not Found kung i-open ang http://127.0.0.1:8000)
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "Telegram Python Server is Running!"})

# 2. Ruta para sa Telegram alerts
@app.route('/trigger-alert', methods=['POST'])
def trigger_alert():
    data = request.json
    print("Alert triggered:", data)
    return jsonify({"success": True})

# 3. Ruta para sa pagkuha sa mga mensahe gikan sa Telegram
@app.route('/get-messages', methods=['GET'])
def get_messages():
    global received_messages
    msgs = received_messages.copy()
    received_messages.clear()
    return jsonify({"messages": msgs})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)