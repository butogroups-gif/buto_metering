from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to receive Daraja callbacks
@app.route('/daraja_callback', methods=['POST'])
def daraja_callback():
    data = request.json
    print("Daraja callback received:", data)  # This will appear in Render logs
    return jsonify({"status": "success"}), 200

# Optional home route to check if the server is running
@app.route('/')
def home():
    return "BUTO Metering Server is running!"

if __name__ == '__main__':
    # Do NOT use debug=True on Render; it's only for local testing
    app.run(host='0.0.0.0', port=10000)
