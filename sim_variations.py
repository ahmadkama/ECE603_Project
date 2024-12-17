import numpy as np
import matplotlib.pyplot as plt
from sim import run_simulation

# Define a wider range of TTL values for each service type
TTL_variations = [
    {'eMBB': 200, 'mMTC': 64, 'URLLC': 125},
    {'eMBB': 150, 'mMTC': 80, 'URLLC': 100},
    {'eMBB': 250, 'mMTC': 50, 'URLLC': 150},
    {'eMBB': 100, 'mMTC': 100, 'URLLC': 100},
    {'eMBB': 300, 'mMTC': 30, 'URLLC': 200},
    {'eMBB': 180, 'mMTC': 90, 'URLLC': 110},
    {'eMBB': 220, 'mMTC': 70, 'URLLC': 130},
    {'eMBB': 130, 'mMTC': 110, 'URLLC': 90}
]

# Run simulations for each TTL variation
average_users = {'eMBB': [], 'mMTC': [], 'URLLC': []}
max_users = {'eMBB': [], 'mMTC': [], 'URLLC': []}
for TTL in TTL_variations:
    result = run_simulation(TTL)
    average_users['eMBB'].append(np.mean(result['embb_counts']))
    average_users['mMTC'].append(np.mean(result['mmtc_counts']))
    average_users['URLLC'].append(np.mean(result['urllc_counts']))
    max_users['eMBB'].append(np.max(result['embb_counts']))
    max_users['mMTC'].append(np.max(result['mmtc_counts']))
    max_users['URLLC'].append(np.max(result['urllc_counts']))

# Plot average users for each service type and TTL variation
x_labels = [f'TTL{i+1}' for i in range(len(TTL_variations))]
x = np.arange(len(x_labels))

plt.figure(figsize=(12, 7))
plt.bar(x - 0.2, average_users['eMBB'], width=0.2, label='eMBB', color='b')
plt.bar(x, average_users['mMTC'], width=0.2, label='mMTC', color='g')
plt.bar(x + 0.2, average_users['URLLC'], width=0.2, label='URLLC', color='r')

plt.xlabel('TTL Variations')
plt.ylabel('Average Number of Active Users')
plt.title('Average Active Users for Each Service Type Across TTL Variations')
plt.xticks(x, x_labels)
plt.legend()
plt.grid(True)
plt.show()

# plot max users
plt.figure(figsize=(12, 7))
plt.bar(x - 0.2, max_users['eMBB'], width=0.2, label='eMBB', color='b')
plt.bar(x, max_users['mMTC'], width=0.2, label='mMTC', color='g')
plt.bar(x + 0.2, max_users['URLLC'], width=0.2, label='URLLC', color='r')

plt.xlabel('TTL Variations')
plt.ylabel('Maximum Number of Active Users')
plt.title('Maximum Active Users for Each Service Type Across TTL Variations')
plt.xticks(x, x_labels)
plt.legend()
plt.grid(True)
plt.show()


