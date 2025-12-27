import random
import time

vehicle_id = 1
roads = ['A', 'B', 'C', 'D']

while True:
    road = random.choice(roads)
    lane = random.randint(1, 3)

    filename = f"lane{road}.txt"

    with open(filename, "a") as f:
        f.write(f"{vehicle_id},{lane}\n")

    print(f"Generated Vehicle {vehicle_id} on Road {road} Lane {lane}")
    vehicle_id += 1

    time.sleep(1)
