import random

def get_sensor_data():
    return {
        "distance": round(random.uniform(10, 100), 2),
        "speed": round(random.uniform(0, 50), 2),
        "status": "running"
    }