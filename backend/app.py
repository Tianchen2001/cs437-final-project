from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    slot_number = data.get('slot')
    print(f"Moving car to slot {slot_number}")
    return jsonify({'message': f'Car moved to slot {slot_number}'}), 200

@app.route('/exit', methods=['POST'])
def exit():
    print("Car is exiting the parking lot")
    return jsonify({'message': 'Car exited the parking lot'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
