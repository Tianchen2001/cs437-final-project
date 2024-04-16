from flask import Flask, request, jsonify
from flask_cors import CORS

from parking_system import ParkingSystem

app = Flask(__name__)
CORS(app)

ps = ParkingSystem()

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    slot_number = data.get('slot')
    print(f"Moving car to slot {slot_number}")
    ps.move_to(slot_number)
    return jsonify({'message': f'Car moved to slot {slot_number}'}), 200

@app.route('/exit', methods=['POST'])
def exit():
    print("Car is exiting the parking lot")
    ps.move_to(None)
    return jsonify({'message': 'Car exited the parking lot'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
