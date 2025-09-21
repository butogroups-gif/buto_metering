from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/daraja_callback', methods=['POST'])
def daraja_callback():
    data = request.json
    print("Daraja callback received:", data)  # <-- this prints JSON in Render logs
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True)
