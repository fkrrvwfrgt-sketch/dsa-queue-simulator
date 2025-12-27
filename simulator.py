import time
from queue_ds import Queue

lanes = {
    "AL2": Queue(), 
    "BL2": Queue(),
    "CL2": Queue(),
    "DL2": Queue()
}

vehicle_counter = 0
print("Traffic Simulator Started\n")

while True:
   vehicle_counter += 1
    lanes["AL2"].enqueue(vehicle_counter)  
    print(f"Vehicle {vehicle_counter} arrived in AL2")


    if lanes["AL2"].size() > 10:
        print("\n PRIORITY MODE: AL2")
        while lanes["AL2"].size() >= 5:
            served = lanes["AL2"].dequeue()
            print(f"Serving Vehicle {served} from AL2")
            time.sleep(1)
        print("Priority cleared. Normal traffic resumes.\n")

   
    else:
        for lane_name in lanes:
            if not lanes[lane_name].is_empty():
                served = lanes[lane_name].dequeue()
                print(f"Serving Vehicle {served} from {lane_name}")
                break

    time.sleep(1)
