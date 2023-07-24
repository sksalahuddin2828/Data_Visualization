import numpy as np
import matplotlib.pyplot as plt

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def twin_prime_conjecture(limit):
    multiples_of_6 = np.arange(6, limit+1, 6)
    twin_primes = []

    for n in multiples_of_6:
        if is_prime(n - 1) and is_prime(n + 1):
            twin_primes.append((n - 1, n + 1))

    return twin_primes

limit = 1000  # You can adjust the limit as per your requirement

twin_primes = twin_prime_conjecture(limit)

# Visualization
x = [pair[0] for pair in twin_primes]
y = [pair[1] for pair in twin_primes]
z = np.zeros(len(twin_primes))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c='r', marker='o')
ax.set_xlabel('n-1')
ax.set_ylabel('n+1')
ax.set_zlabel('')

plt.title('Twin Prime Conjecture')
plt.show()
