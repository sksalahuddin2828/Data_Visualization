import numpy as np
import plotly.graph_objects as go

# Boolean Algebra Laws
def prove_boolean_algebra_laws():
    A, B = symbols('A B')
    
    commutative_law = Eq(A & B, B & A)
    associative_law = Eq((A & B) & B, A & (B & B))
    distributive_law = Eq(A & (B | B), (A & B) | (A & B))
    demorgans_law_1 = Eq(Not(A & B), Not(A) | Not(B))
    demorgans_law_2 = Eq(Not(A | B), Not(A) & Not(B))
    
    laws = [commutative_law, associative_law, distributive_law, demorgans_law_1, demorgans_law_2]
    
    for idx, law in enumerate(laws, start=1):
        print(f"Law {idx}: {law}")
        proof = law.simplify()
        print("Proof:", proof)
        print("\n")

# Fibonacci Sequence using Recursion
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Prime Number Generator
def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = all(num % i != 0 for i in range(2, int(np.sqrt(num)) + 1))
        if is_prime:
            primes.append(num)
    return primes

# Binomial Coefficient Calculation
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Animate Fibonacci Sequence
def animate_fibonacci(n_terms):
    fig, ax = plt.subplots()
    x_vals = list(range(n_terms))
    y_vals = [fibonacci_recursive(i) for i in x_vals]
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        line.set_data(x_vals[:i], y_vals[:i])
        return line,

    anim = FuncAnimation(fig, animate, init_func=init, frames=n_terms, interval=500, blit=True)
    plt.close(fig)  # Prevents the initial empty plot from displaying
    display(anim)

# Probability Calculation
def calculate_probability(favorable_outcomes, total_outcomes):
    return favorable_outcomes / total_outcomes

# Visualize 3D Surface Plot
def visualize_surface_plot():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z)])
    fig.update_layout(title="3D Surface Plot of sin(sqrt(x^2 + y^2))")
    fig.show()

# Visualize Prime Numbers
def visualize_primes(limit):
    primes = generate_primes(limit)
    plt.figure(figsize=(8, 6))
    plt.scatter(primes, [1] * len(primes), color='green', marker='o')
    plt.title(f"Visualization of Prime Numbers up to {limit}")
    plt.xlabel("Prime Numbers")
    plt.yticks([])
    plt.grid(axis='x')
    plt.show()

# Run examples
prove_boolean_algebra_laws()

n_terms = 10
animate_fibonacci(n_terms)

limit = 50
visualize_primes(limit)

n = 5
k = 2
binomial_result = binomial_coefficient(n, k)
print(f"Binomial Coefficient C({n}, {k}):", binomial_result)

count_passwords()

# Visualize 3D Surface Plot
visualize_surface_plot()
