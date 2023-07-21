import math

def binomial_probability(n, p, k):
    """Calculate the binomial probability of obtaining k successes in n trials with probability p."""
    q = 1 - p
    return math.comb(n, k) * (p ** k) * (q ** (n - k))

def binomial_distribution_calculator():
    print("Binomial Distribution Calculator")
    print("--------------------------------")

    # Get user inputs
    n = int(input("Enter the number of trials (n): "))
    p = float(input("Enter the probability of success (p): "))
    k = int(input("Enter the number of successful events (k): "))

    # Calculate the probability
    probability = binomial_probability(n, p, k)

    # Print the result
    print(f"The probability of obtaining {k} successful events in {n} trials with a probability of {p:.4f} is {probability:.4f}.")

if __name__ == "__main__":
    binomial_distribution_calculator()


  
# Answer: Binomial Distribution Calculator
#         --------------------------------
#         Enter the number of trials (n): 10
#         Enter the probability of success (p): 23
#         Enter the number of successful events (k): 12
#         The probability of obtaining 12 successful events in 10 trials with a probability of 23.0000 is 0.0000.
