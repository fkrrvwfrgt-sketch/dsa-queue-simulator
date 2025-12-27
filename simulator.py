import time
from queue_ds import Queue

AL2 = Queue()

vehicle_counter = 0

print("Traffic Simulator Started...\n")

while True:
  
    vehicle_counter += 1
    AL2.enqueue(vehicle_counter)
    print(f"Vehicle {vehicle_counter} arrived in AL2")

 
    if AL2.size() > 10:
        print("\n PRIORITY MODE ACTIVATED")

        while AL2.size() >= 5:
            served_vehicle = AL2.dequeue()
            print(f"Serving vehicle {served_vehicle} from AL2")
            time.sleep(1)

        print("Priority cleared, returning to normal mode\n")

    time.sleep(1)
