import plotly.express as px

# Calculate the total number of possible hands
total_hands = comb(52, 5)

# Calculate the number of three-of-a-kind hands
three_of_a_kind_hands = 13 * comb(4, 3) * comb(12, 2) * comb(4, 1) * comb(4, 1)

# Calculate the probability of getting a three-of-a-kind hand
probability_three_of_a_kind = three_of_a_kind_hands / total_hands

# Create a pie chart to visualize the probabilities
labels = ['Three-of-a-Kind', 'Other Hands']
values = [probability_three_of_a_kind, 1 - probability_three_of_a_kind]

fig = px.pie(values=values, names=labels, title='Probability of Getting a Three-of-a-Kind Poker Hand',
             template='plotly_dark')
fig.update_traces(textinfo='percent+label', pull=0.05)
fig.show()
