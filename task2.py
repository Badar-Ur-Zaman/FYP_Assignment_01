import numpy as np
import matplotlib.pyplot as plt

# Part 01 - Network Model: 100 Users and 1 Base Station

area_size = 500
num_users = 100

# Generate uniformly distributed x and y coordinates for users
x_users = np.random.uniform(0, area_size, num_users)
y_users = np.random.uniform(0, area_size, num_users)