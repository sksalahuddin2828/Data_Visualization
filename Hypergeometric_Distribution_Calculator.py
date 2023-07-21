import math

def hypergeometric_probability(population_size, success_population, sample_size, successes):
    """Calculate the hypergeometric probability of obtaining 'successes' successes in 'sample_size' draws
    from a population of size 'population_size' with 'success_population' successes."""
    return (math.comb(success_population, successes) * math.comb(population_size - success_population, sample_size - successes)) / math.comb(population_size, sample_size)

def hypergeometric_distribution_calculator():
    print("Hypergeometric Distribution Calculator")
    print("-------------------------------------")

    # Get user inputs
    population_size = int(input("Enter the population size: "))
    success_population = int(input("Enter the number of successes in the population: "))
    sample_size = int(input("Enter the sample size (number of draws): "))
    successes = int(input("Enter the desired number of successes in the draws: "))

    # Calculate the probability
    probability = hypergeometric_probability(population_size, success_population, sample_size, successes)

    # Print the result
    print(f"The probability of obtaining {successes} successes in {sample_size} draws from a population of size {population_size} with {success_population} successes is {probability:.4f}.")

if __name__ == "__main__":
    hypergeometric_distribution_calculator()



# Answer: Hypergeometric Distribution Calculator
#         -------------------------------------
#         Enter the population size: 100000
#         Enter the number of successes in the population: 10000
#         Enter the sample size (number of draws): 1250
#         Enter the desired number of successes in the draws: 142
#         The probability of obtaining 142 successes in 1250 draws from a population of size 100000 with 10000 successes is 0.0102.
