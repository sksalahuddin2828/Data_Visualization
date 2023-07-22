import numpy as np
import plotly.graph_objects as go

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
    fig = go.Figure()

    for even_num, primes in combinations.items():
        num_combinations = len(primes)
        for i, prime_pair in enumerate(primes):
            x = [even_num]
            y = [prime_pair[0]]
            z = [prime_pair[1]]
            size = 5 + 15 * (1 - i/num_combinations)
            color = i / num_combinations

            # Plot 3D scatter points representing the prime pairs
            fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers',
                                       marker=dict(size=size, color=color, colorscale='Viridis'),
                                       text=f"{even_num} = {prime_pair[0]} + {prime_pair[1]}"))

    fig.update_layout(scene=dict(xaxis_title='Even Numbers', yaxis_title='First Prime', zaxis_title='Second Prime'),
                      scene_aspectmode='cube', title="Goldbach's Conjecture 3D Visualization")
    
    fig.show()

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
