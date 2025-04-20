import numpy as np
import matplotlib.pyplot as plt
#given data
pt = 1
dh = np.arange(20, 70, 5)
dv = 2
n = np.array([3, 3.5, 4]) 
N = 10000  # number of samples
variance = 1 # rayleigh fading variance is 1

alpha = variance/2
x = np.random.randn(N)
y = np.random.randn(N)
c = x + 1j*y
g = np.sqrt(alpha) * np.abs(c)
g = np.abs(g)**2 # g is the rayleigh fading channel gain
d = np.sqrt(dh**2 + dv**2)
