import matplotlib.pyplot as plt

def P(n):
    return 11*n**2 + 122*n + 1

def prove_divisibility_by_133(n):
    for i in range(1, n+1):
        if P(i) % 133 != 0:
            return False
    return True

# Visualize P(n) for n from 1 to 20
n_values = list(range(1, 21))
P_values = [P(n) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, P_values, marker='o', color='b')
plt.axhline(y=133, color='r', linestyle='--', label='y = 133')
plt.xlabel('n')
plt.ylabel('P(n)')
plt.title('P(n) = 11n^2 + 122n + 1')
plt.legend()
plt.grid(True)
plt.show()

# Prove for n=20
n = 20
if prove_divisibility_by_133(n):
    print(f"P(n) is divisible by 133 for n = {n}")
else:
    print(f"P(n) is not divisible by 133 for n = {n}")
