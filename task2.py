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