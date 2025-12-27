# Assignment 1: Queue Based Traffic Light Simulator

## Name:Sara Basnet
## Roll Number:10
## Course: COMP202

## Summary
This project simulates a traffic junction using queue data structures. Vehicles are generated randomly and processed using FIFO queues. A priority lane is handled when vehicle count exceeds a threshold.

## Data Structures Used

| Data Structure | Implementation | Purpose |
|---------------|---------------|--------|
| Queue | Python list | Store vehicles per lane |

## Functions Implemented
- enqueue()
- dequeue()
- size()
- is_empty()

## Traffic Algorithm
1. Generate vehicles
2. Add vehicles to queues
3. Check priority lane condition
4. Serve vehicles
5. Resume normal operation

## Time Complexity
- Enqueue: O(1)
- Dequeue: O(n)
- Priority check: O(1)

## GitHub Repository
(put your repo link here)
