import plotly.graph_objects as go

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

# Create labels for the categories
labels = ['All three newspapers', 'Newspaper A only', 'Newspaper B only', 'Newspaper C only',
          'None of A, B, C', 'Exactly one newspaper', 'Newspaper A and B only',
          'Newspaper B and C only', 'Newspaper C and A only', 'At least two newspapers',
          'At most two newspapers', 'Exactly two newspapers']

# Create a list of percentages for each category
percentages = [n_A_and_B_and_C/total_families*100, n_A_only/total_families*100, n_B_only/total_families*100,
               n_C_only/total_families*100, n_none/total_families*100, n_exactly_one/total_families*100,
               n_A_and_B_only/total_families*100, n_B_and_C_only/total_families*100,
               n_A_and_C_only/total_families*100, n_at_least_two/total_families*100,
               n_at_most_two/total_families*100, n_exactly_two/total_families*100]

# Create a Pie trace
fig = go.Figure(data=[go.Pie(labels=labels, values=percentages, marker=dict(colors=colors))])

# Create a layout
fig.update_layout(title='Family Newspaper Preferences',
                  scene=dict(camera=dict(up=dict(x=0, y=0, z=1), center=dict(x=0, y=0, z=0))),
                  showlegend=False)

# Show the plot
fig.show()
