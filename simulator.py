import threading
import time
from queue_ds import Queue
from traffic_generator import generate_vehicles

lanes = {
    "AL2": Queue(),  
    "BL2": Queue(),
    "CL2": Queue(),
    "DL2": Queue(),
    "A1": Queue(),
    "B1": Queue(),
    "C1": Queue(),
    "D1": Queue(),
    "A3": Queue(), 
    "B3": Queue(),
    "C3": Queue(),
    "D3": Queue()
}

def traffic_simulator():
    normal_lanes = ["A1", "B1", "C1", "D1"]
    left_turn_lanes = ["A3", "B3", "C3", "D3"]

    while True:
    
        if lanes["AL2"].size() > 10:
            print("\n=== PRIORITY MODE: AL2 ===")
            while lanes["AL2"].size() >= 5:
                served = lanes["AL2"].dequeue()
                print(f"Serving Vehicle {served} from AL2")
                time.sleep(1)
            print("Priority cleared. Normal traffic resumes.\n")
        else:
            
            for lane_name in normal_lanes:
                if not lanes[lane_name].is_empty():
                    served = lanes[lane_name].dequeue()
                    print(f"Serving Vehicle {served} from {lane_name}")
                    break
         
            for lane_name in left_turn_lanes:
                if not lanes[lane_name].is_empty():
                    served = lanes[lane_name].dequeue()
                    print(f"Serving Vehicle {served} from left-turn lane {lane_name}")
                    break

        time.sleep(1)

def print_lane_status():
    while True:
        status = {lane: lanes[lane].size() for lane in lanes}
        print("Lane Status:", status)
        time.sleep(3)

if __name__ == "__main__":
    print("Traffic Simulator Started\n")

   
    generator_thread = threading.Thread(target=generate_vehicles, args=(lanes,))
    simulator_thread = threading.Thread(target=traffic_simulator)
    status_thread = threading.Thread(target=print_lane_status)

    generator_thread.start()
    simulator_thread.start()
    status_thread.start()

    generator_thread.join()
    simulator_thread.join()
    status_thread.join()

   
