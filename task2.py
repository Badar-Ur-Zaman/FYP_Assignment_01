# Task 02 - Part 01: Network Model with 100 Users and 1 Base Station

import numpy as np
import matplotlib.pyplot as plt

# Simulation Parameters
area_size = 500           # Square area size (500 x 500)
num_users = 100           # Number of users
iterations = 1000         # Try values 1,10,100 for Monte Carlo iterations 


# In our simulation, each iteration generates a new random realization of:
# Rayleigh fading channels
# Received power and SNR
# Outage condition (rate < threshold)
# The more iterations we run, the more accurately we can approximate the true statistical behavior of the system. 
# That's we see change in curve as we decrease the number of iterations


p_t = 1                   # Transmit power in Watts
varience = 0.5            # Variance of Rayleigh fading
n = 3.5                   # Path loss exponent

# Noise power in dBm → convert to Watts
N_dBm = -96
N = 10 ** ((N_dBm - 30) / 10)

# Threshold values (in bps/Hz) to evaluate outage probability
threshold_values = np.arange(0, 26, 5) 
# Initialize list to store mean outage probabilities
outage_prob_list = []

# Main Loop over each threshold
for rate_t in threshold_values:
    outage_count = np.zeros(num_users)  # Reset outage count

    # Monte Carlo Simulation
    for _ in range(iterations):
       
        x_users = np.random.uniform(0, area_size, num_users)
        y_users = np.random.uniform(0, area_size, num_users)

        # Base Station at (0, 0)
        x_bs, y_bs = 0, 0

        # Compute distance from BS and path loss
        distance = np.sqrt((x_users - x_bs)**2 + (y_users - y_bs)**2)
        path_loss = 1 / (distance ** n)

        # Rayleigh fading (complex Gaussian)
        x = np.sqrt(varience) * np.random.randn(num_users)
        y = np.sqrt(varience) * np.random.randn(num_users)
        h = np.abs(x + 1j * y) ** 2

        # Received power: Pr = Pt * |h|^2 * path_loss
        p_r = p_t * path_loss * h

        # SNR and Rate
        snr = p_r / N
        rate = np.log2(1 + snr)

        # Count outages
        outage_count += (rate < rate_t)

    # Compute outage probability for this threshold
    outage_prob = outage_count / iterations
    print(f"Threshold Rate: {rate_t} bps/Hz, Outage Probability: {np.mean(outage_prob)}")
    outage_prob_list.append(np.mean(outage_prob))  # Mean over all users

# Plot: Total Outage Probability vs Threshold Rate
plt.figure(figsize=(8, 6))
plt.plot(threshold_values, outage_prob_list, marker='o', linestyle='-', color='b')

# As we increase 𝜏:
# The condition 
# log 2(1+SNR) <𝜏 becomes harder to satisfy
# So more users fail to meet the requirement
# Hence, more users are in outage
# That’s why the outage probability increases.

plt.title("Total Outage Probability vs Threshold Rate ")
plt.xlabel("Threshold Rate [bps/Hz]")
plt.ylabel("Total Outage Probability")
plt.grid(True)
plt.tight_layout()
plt.show()