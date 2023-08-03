import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given data
total_families = 10000
n_A = 0.4 * total_families
n_B = 0.2 * total_families
n_C = 0.1 * total_families
n_A_and_B = 0.05 * total_families
n_B_and_C = 0.03 * total_families
n_A_and_C = 0.04 * total_families
n_A_and_B_and_C = 0.02 * total_families

# Calculate the number of families which buy each category
n_A_only = n_A - n_A_and_B - n_A_and_C + n_A_and_B_and_C
n_B_only = n_B - n_A_and_B - n_B_and_C + n_A_and_B_and_C
n_C_only = n_C - n_A_and_C - n_B_and_C + n_A_and_B_and_C
n_none = total_families - (n_A + n_B + n_C - n_A_and_B - n_A_and_C - n_B_and_C + n_A_and_B_and_C)
n_exactly_one = n_A_only + n_B_only + n_C_only
n_A_and_B_only = n_A_and_B - n_A_and_B_and_C
n_B_and_C_only = n_B_and_C - n_A_and_B_and_C
n_A_and_C_only = n_A_and_C - n_A_and_B_and_C
n_at_least_two = n_A_and_B_and_C
n_at_most_two = total_families - n_none
n_exactly_two = n_A_and_B_and_C

# Create a DataFrame to store the results
results_df = pd.DataFrame({
    'Category': ['All three newspapers', 'Newspaper A only', 'Newspaper B only', 'Newspaper C only',
                 'None of A, B, C', 'Exactly one newspaper', 'Newspaper A and B only',
                 'Newspaper B and C only', 'Newspaper C and A only', 'At least two newspapers',
                 'At most two newspapers', 'Exactly two newspapers'],
    'Percentage': [n_A_and_B_and_C/total_families*100, n_A_only/total_families*100, n_B_only/total_families*100,
                   n_C_only/total_families*100, n_none/total_families*100, n_exactly_one/total_families*100,
                   n_A_and_B_only/total_families*100, n_B_and_C_only/total_families*100,
                   n_A_and_C_only/total_families*100, n_at_least_two/total_families*100,
                   n_at_most_two/total_families*100, n_exactly_two/total_families*100]
})

# 3D Visualization using a pie chart
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Convert percentage to radians
theta = results_df['Percentage'] * (2 * np.pi / 100)

# Set the z-axis for each category
z = results_df.index

# Plot the pie chart for each category
for i, (color, label) in enumerate(zip(['r', 'b', 'g', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'lime', 'pink', 'skyblue', 'darkviolet'], results_df['Category'])):
    ax.bar3d(0, i, z[i], theta[i], 0.5, 0.5, color=color)
    ax.text(0.5, i + 0.2, z[i] + 0.25, f'{results_df["Percentage"][i]:.2f}%', ha='center', fontsize=8, color='black')
    ax.text(2, i, z[i] + 0.25, label, ha='center', fontsize=8, color='black')

# Hide grid lines and axes
ax.grid(False)
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlabel('Percentage')

# Set the title
ax.set_title('Family Newspaper Preferences', fontsize=14)

plt.show()
