# 1. Series and Parallel Resistance:
# (a) Series Resistance (R1 + R2):
# When two resistors, R1 and R2, are connected in series, their resistances simply add up:

def series_resistance(R1, R2):
    return R1 + R2

R1 = 1000  # Example values
R2 = 10

series_result = series_resistance(R1, R2)
print(f"Series Resistance: {series_result}")

# (b) Parallel Resistance (1 / R_parallel = 1 / R1 + 1 / R2):
# When two resistors, R1 and R2, are connected in parallel, their reciprocals add up:

def parallel_resistance(R1, R2):
    return 1 / (1 / R1 + 1 / R2)

parallel_result = parallel_resistance(R1, R2)
print(f"Parallel Resistance: {parallel_result}")

def find_second_resistance(total_resistance, first_resistance):
    return 1 / (1 / total_resistance - 1 / first_resistance)

total_resistance = 150
first_resistance = 145

second_resistance = find_second_resistance(total_resistance, first_resistance)
print(f"Second Resistance: {second_resistance}")

# Answer: Series Resistance: 1010
#         Parallel Resistance: 9.900990099009901
#         Second Resistance: -4350.00000000001

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data
R1_values = np.linspace(1, 1000, 50)
R2_values = np.linspace(1, 100, 50)
R1, R2 = np.meshgrid(R1_values, R2_values)
series_resistances = R1 + R2
parallel_resistances = 1 / (1 / R1 + 1 / R2)

# Plot series resistance
ax.plot_surface(R1, R2, series_resistances, cmap='viridis')
ax.set_xlabel('R1')
ax.set_ylabel('R2')
ax.set_zlabel('Series Resistance')
ax.set_title('Series Resistance Visualization')

plt.show()
