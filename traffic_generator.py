import random
import time
from queue_ds import Queue

def generate_vehicles(lanes):
    vehicle_id = 1
    lane_names = list(lanes.keys())
    while True:
        lane = random.choice(lane_names)  # Random lane
        lanes[lane].enqueue(vehicle_id)
        print(f"Vehicle {vehicle_id} generated in {lane}")
        vehicle_id += 1
        time.sleep(1)
