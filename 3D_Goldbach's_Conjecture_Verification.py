import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_conjecture(limit):
    even_numbers = [num for num in range(4, limit + 1, 2)]
    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    
    # Dictionary to store the combinations for each even number
    combinations = {num: [] for num in even_numbers}
    
    for even_num in even_numbers:
        for prime in primes:
            if prime >= even_num:
                break
            complement = even_num - prime
            if is_prime(complement):
                combinations[even_num].append((prime, complement))
    
    return combinations

# Let's verify Goldbach's Conjecture for even numbers up to a certain limit
limit = 100
result = goldbach_conjecture(limit)

for even_num, combinations in result.items():
    print(f"{even_num} = " + " + ".join([f"{x[0]} + {x[1]}" for x in combinations]))

# Visualization (Not 3D since primes do not have spatial relationships)
x = list(result.keys())
y = [len(combinations) for combinations in result.values()]

plt.bar(x, y)
plt.xlabel("Even Numbers")
plt.ylabel("Number of Combinations")
plt.title("Goldbach's Conjecture Verification")
plt.show()
