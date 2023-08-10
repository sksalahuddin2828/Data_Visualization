import plotly.express as px

# Create an interactive scatter plot
df = px.data.iris()
scatter = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
scatter.show()
