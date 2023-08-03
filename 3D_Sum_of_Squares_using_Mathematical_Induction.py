import matplotlib.pyplot as plt

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

# Prove using mathematical induction
def prove_sum_of_squares(n):
    for i in range(1, n+1):
        if sum_of_squares(i) != i*(i+1)*(2*i+1)//6:
            return False
    return True

# Visualize the sum of squares
n_values = list(range(1, 11))
sum_squares_values = [sum_of_squares(n) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, sum_squares_values, marker='o', color='b', label='Sum of Squares')
plt.plot(n_values, [n*(n+1)*(2*n+1)//6 for n in n_values], marker='x', color='r', label='n*(n+1)*(2n+1)//6')
plt.xlabel('n')
plt.ylabel('Sum of Squares')
plt.title('Sum of Squares using Mathematical Induction')
plt.legend()
plt.grid(True)
plt.show()

# Prove for n=10
n = 10
if prove_sum_of_squares(n):
    print(f"Sum of squares is true for n = {n}")
else:
    print(f"Sum of squares is not true for n = {n}")
