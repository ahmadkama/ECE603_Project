import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

# Simulation parameters
HOURS = 24
SECONDS_PER_HOUR = 3600
TOTAL_SECONDS = HOURS * SECONDS_PER_HOUR
SAMPLE_INTERVAL = 15 * 60  # 15 minutes in seconds

# Traffic distribution (250,000 total requests)
TOTAL_REQUESTS = 250000
REQUESTS_PER_SEC = TOTAL_REQUESTS / TOTAL_SECONDS
EMBB_FRACTION = 0.40  # 40% eMBB
MMTC_FRACTION = 0.25  # 25% mMTC 
URLLC_FRACTION = 0.35 # 35% URLLC

# TTL in seconds for each service type
TTL = {
    'eMBB': 300,  # 5 minutes - longer TTL for broadband
    'mMTC': 30,   # 30 seconds
    'URLLC': 10   # 10 seconds
}

# Track active connections
active_connections = {
    'eMBB': deque(),
    'mMTC': deque(), 
    'URLLC': deque()
}

# Simulation results storage
timestamps = []
embb_counts = []
mmtc_counts = []
urllc_counts = []

# Run simulation
current_time = 0
while current_time < TOTAL_SECONDS:
    
    # Generate new connections based on Poisson distribution
    num_new = np.random.poisson(REQUESTS_PER_SEC)
    for _ in range(num_new):
        rand = random.random()
        if rand < EMBB_FRACTION:
            active_connections['eMBB'].append(current_time + TTL['eMBB'])
        elif rand < EMBB_FRACTION + MMTC_FRACTION:
            active_connections['mMTC'].append(current_time + TTL['mMTC'])
        else:
            active_connections['URLLC'].append(current_time + TTL['URLLC'])
    
    # Remove expired connections
    for service in active_connections:
        while active_connections[service] and active_connections[service][0] <= current_time:
            active_connections[service].popleft()
    
    # Record stats every 15 minutes after first hour
    if current_time >= 3600 and current_time % SAMPLE_INTERVAL == 0:
        timestamps.append(current_time/3600)  # Convert to hours
        embb_counts.append(len(active_connections['eMBB']))
        mmtc_counts.append(len(active_connections['mMTC']))
        urllc_counts.append(len(active_connections['URLLC']))
        
    current_time += 1

# Plot results
plt.figure(figsize=(12,6))
plt.plot(timestamps, embb_counts, 'b-', label='eMBB', linewidth=2)
plt.plot(timestamps, mmtc_counts, 'g-', label='mMTC', linewidth=2)
plt.plot(timestamps, urllc_counts, 'r-', label='URLLC', linewidth=2)
plt.xlabel('Time (hours)')
plt.ylabel('Number of Active Users')
plt.title('Network Slice Usage Over 24 Hours (15-minute intervals)')
plt.legend()
plt.grid(True)
plt.xticks(np.arange(1, 25, 2))  # Show every 2 hours on x-axis
plt.show()

# Print average counts
print(f"Average eMBB users: {np.mean(embb_counts):.0f}")
print(f"Average mMTC users: {np.mean(mmtc_counts):.0f}")
print(f"Average URLLC users: {np.mean(urllc_counts):.0f}")

