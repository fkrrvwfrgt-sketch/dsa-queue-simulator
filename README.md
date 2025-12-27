# Assignment 1 - Traffic Light Simulator
**Course:** Data Structures and Algorithms (COMP202)  
**Name:** Sara Basnet
**Roll Number:** 10

## Summary
This project simulates a traffic junction with 4 roads (A,B,C,D) and 3 lanes each. The program implements vehicle queues using a queue data structure. Priority lane AL2 is served first if more than 10 vehicles are waiting. Normal lanes are served round-robin. Left-turn lanes are served if available.

## Data Structures Used
- **Queue:** FIFO queue implemented in `queue_ds.py`  
- **Dictionary:** For storing all lane queues  

## Functions Implemented
- `enqueue(item)`  
- `dequeue()`  
- `size()`  
- `generate_vehicles(lanes)`  
- `traffic_simulator()`  
- `print_lane_status()`  

## Algorithm
1. Generate vehicles randomly for all lanes.  
2. If AL2 has >10 vehicles → serve AL2 until <5 vehicles.  
3. Serve normal lanes in round-robin.  
4. Serve left-turn lanes if vehicles present.  

## Time Complexity
- Enqueue: O(1)  
- Dequeue: O(n) (because we use list pop(0))  

## How to Run
1. Open terminal in `dsa-queue-simulator` folder.  
2. Run:
```bash
python simulator.py
