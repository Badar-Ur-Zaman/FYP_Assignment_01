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

final_result = np.zeros(len(dh))  # Initially, result is 0

for n_value in n:
    result = []
    for d_value in d:
        temp = (d_value**(-n_value)) * g
        avg_temp = np.mean(temp)
        result.append(avg_temp)
    iter_i = pt * np.array(result)
    final_result += iter_i

Pr = final_result/len(n)
print(Pr)

plt.title("Received Power vs Horizontal Distance")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Received Power (Watts)")
plt.plot(dh, Pr, 'r--', label='Received Power')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()