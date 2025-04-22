import numpy as np
import matplotlib.pyplot as plt

# Part 01 - Network Model: 100 Users and 1 Base Station

area_size = 500
num_users = 100

# Generate uniformly distributed x and y coordinates for users
x_users = np.random.uniform(0, area_size, num_users)
y_users = np.random.uniform(0, area_size, num_users)

# Base Station at origin (0, 0)
x_bs, y_bs = 0, 0

# Plot the network
plt.scatter(x_users, y_users, c='blue', label='Users')
plt.scatter(x_bs, y_bs, c='red',marker='*',s=100, label='Base Station')
plt.title("Network Model: 100 Users and 1 Base Station")
plt.xlabel("X coordinate (m)")
plt.ylabel("Y coordinate (m)")
plt.legend()
plt.grid()
plt.show()

# Part 02 - Distance between Users and Base Station
distance = np.zeros(num_users)
path_loss = np.zeros(num_users)
varience = 0.5  
n = 3.5  # Path loss exponent 

 # Calculate distances and path loss
for d in range(num_users):
    distance[d] = np.sqrt((x_users[d] - x_bs) ** 2 + (y_users[d] - y_bs) ** 2)
    # Part 3 - Path Loss Calculation
    path_loss[d] = 1 / distance[d] ** n
print(f"Distance from BS to each user: ", distance)
print(f"Path loss for each user when path loss exponent is 3.5 : ", path_loss)

# Part 4 - Calculating Recieved Power
# Calculate Rayleigh fading channel
x = np.sqrt(varience) * np.random.randn(num_users)
y = np.sqrt(varience) * np.random.randn(num_users)
g = x + 1j * y
h = np.abs(g) ** 2
print(f"Rayleigh fading channel gain for each user: ", h)

pr = np.zeros(num_users)
pt = 1 # Watts
snr = np.zeros(num_users)
rate = np.zeros(num_users)
N = -96 # Noise power in dBm
N = 10 ** ((N-30)/ 10) # Convert dBm to Watts
rate_t = 1 # Threshold rate in bps/Hz

# Calculate received power
for i in range(num_users):
    pr[i] = pt * path_loss[i] * h[i]
print(f"Received power for each user: ", pr)

# Initialize outage count for each user
outage_count = np.zeros(num_users)
outage_prob = np.zeros(num_users)

# Part 5 - Calculate SNR and rate
for i in range(num_users):
    snr[i] = pr[i] / N
    rate[i] = np.log2(1 + snr[i])
    # Update outage count if rate is below threshold
    
    # Part 7 - Outage Probability Calculation
    if rate[i] < rate_t:
        outage_count[i] += 1  # Increment outage count for the user

print(f"SNR for each user: ", snr)
print(f"Rate for each user: ", rate)