import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes_up_to_limit(limit):
    return [num for num in range(2, limit + 1) if is_prime(num)]

def goldbach_combinations(limit):
    even_numbers = [num for num in range(4, limit + 1, 2)]
    primes = primes_up_to_limit(limit)
    
    combinations = {num: [] for num in even_numbers}
    
    for even_num in even_numbers:
        for prime in primes:
            if prime >= even_num:
                break
            complement = even_num - prime
            if is_prime(complement):
                combinations[even_num].append((prime, complement))
    
    return combinations

def visualize_goldbach_combinations(combinations):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for even_num, primes in combinations.items():
        x = even_num
        y = [p[0] for p in primes]
        z = [p[1] for p in primes]
        num_combinations = len(primes)

        # Plot the 3D bars with color based on the number of combinations
        ax.bar3d([x], [y[0]], [z[0]], dx=0.5, dy=0.5, dz=num_combinations, shade=True, alpha=0.8, color=plt.cm.jet(num_combinations/len(combinations)))

        # Annotate the bars with the number of combinations
        ax.text(x + 0.25, y[0], z[0] + num_combinations, f"{num_combinations}", fontsize=8, ha='center', va='bottom')

    ax.set_xlabel('Even Numbers')
    ax.set_ylabel('First Prime')
    ax.set_zlabel('Second Prime')
    ax.set_title("Goldbach's Conjecture 3D Visualization")

    plt.show()

def print_goldbach_combinations(combinations):
    for even_num, primes in combinations.items():
        print(f"{even_num} = " + " + ".join([f"{x[0]} + {x[1]}" for x in primes]))

# Let's verify Goldbach's Conjecture for even numbers up to a certain limit
limit = 100
combinations = goldbach_combinations(limit)

# Print the combinations for each even number
print_goldbach_combinations(combinations)

# Visualize the combinations in 3D plot
visualize_goldbach_combinations(combinations)
