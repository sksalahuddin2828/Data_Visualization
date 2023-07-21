import math

def binomial_probability(n, p, k):
    q = 1 - p
    return math.comb(n, k) * (p ** k) * (q ** (n - k))

n = 20
p = 0.10
cumulative_probability = sum(binomial_probability(n, p, k) for k in range(4))

print(f"The likelihood of obtaining ≤ 3 statisticians in the sample is {cumulative_probability:.4f}.")


# Answer: The likelihood of obtaining ≤ 3 statisticians in the sample is 0.8670.
