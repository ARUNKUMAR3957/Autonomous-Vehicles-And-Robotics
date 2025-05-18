from flask import Flask, render_template, Response, jsonify
from camera import gen_camera_stream
from sensors import get_sensor_data
from controller import start_autonomous_mode, stop_car

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_camera_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start', methods=['POST'])
def start():
    start_autonomous_mode()
    return jsonify({"status": "Autonomous mode started"})

@app.route('/stop', methods=['POST'])
def stop():
    stop_car()
    return jsonify({"status": "Car stopped"})

@app.route('/sensors', methods=['GET'])
def sensors():
    data = get_sensor_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)