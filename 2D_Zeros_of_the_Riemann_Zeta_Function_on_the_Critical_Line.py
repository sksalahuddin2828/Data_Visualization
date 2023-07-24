import numpy as np
import matplotlib.pyplot as plt

def zeta(s):
    return np.sum(1 / np.power(np.arange(1, 10000), s))

def zeta_critical_line(t):
    s = 0.5 + 1j * t
    return zeta(s).real

t_values = np.linspace(0, 81702130.19, 500)
zeta_values = [zeta_critical_line(t) for t in t_values]

plt.figure(figsize=(12, 6))
plt.plot(t_values, zeta_values, label='Riemann Zeta Function on Critical Line', color='blue')
plt.xlabel('t')
plt.ylabel('zeta(1/2 + it)')
plt.title('Riemann Zeta Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()

def find_zeros(t_range):
    zeros = []
    for t in t_range:
        s = 0.5 + 1j * t
        z = zeta(s)
        if abs(z) < 1e-8:
            zeros.append(t)
    return zeros

t_values = np.linspace(0, 81702130.19, 2000)
zeros = find_zeros(t_values)

plt.figure(figsize=(12, 6))
plt.plot(t_values, np.zeros(len(t_values)), label='Critical Line', color='black')
plt.scatter(zeros, np.zeros(len(zeros)), color='red', marker='o', label='Zeros on Critical Line')
plt.xlabel('t')
plt.title('Zeros of the Riemann Zeta Function on the Critical Line')
plt.legend()
plt.grid(True)
plt.show()
