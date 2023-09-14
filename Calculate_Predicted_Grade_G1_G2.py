import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create synthetic student data (example)
# Replace this with your own data if available
data = {
    'G1': [10, 12, 15, 18, 20],
    'G2': [11, 14, 16, 19, 21],
    'final_grade': [11, 13, 16, 18, 20]
}

# Convert data to a DataFrame (optional)
df = pd.DataFrame(data)

# Independent variables (G1 and G2 scores)
X = df[['G1', 'G2']].values

# Dependent variable (final grade)
y = df['final_grade'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Define student data for prediction
student_data = np.array([[15, 18]])  # Replace with the actual G1 and G2 scores

# Make predictions using the model
predicted_grade = model.predict(student_data)

print(f'Predicted Grade: {predicted_grade[0]}')  # Print the predicted grade

# Answer: Predicted Grade: 16.471365638766517


#----------------------------------------------------------------------------------------------------------


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib  # Import joblib for model persistence

# Create synthetic student data (example)
# Replace this with your own data if available
data = {
    'G1': [10, 12, 15, 18, 20],
    'G2': [11, 14, 16, 19, 21],
    'final_grade': [11, 13, 16, 18, 20]
}

# Convert data to a DataFrame (optional)
df = pd.DataFrame(data)

# Independent variables (G1 and G2 scores)
X = df[['G1', 'G2']].values

# Dependent variable (final grade)
y = df['final_grade'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model using scikit-learn's joblib-based functionality
joblib.dump(model, 'trained_model.pkl')

# Load the pre-trained model (for prediction)
loaded_model = joblib.load('trained_model.pkl')

# Define student data for prediction
student_data = np.array([[15, 18]])  # Replace with the actual G1 and G2 scores

# Make predictions using the loaded model
predicted_grade = loaded_model.predict(student_data)

print(f'Predicted Grade: {predicted_grade[0]}')  # Print the predicted grade


#--------------------------------------------------------------------------------------------------------------


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib  # Import joblib for model persistence

# Load and preprocess the dataset
data = pd.read_csv('student_data.csv')  # Replace with your dataset file
X = data[['G1', 'G2']].values  # Independent variables (G1 and G2 scores)
y = data['final_grade'].values  # Dependent variable (final grade)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model using scikit-learn's joblib-based functionality
joblib.dump(model, 'trained_model.pkl')

# Load the pre-trained model (for prediction)
loaded_model = joblib.load('trained_model.pkl')

# Define student data for prediction
student_data = np.array([[15, 18]])  # Replace with the actual G1 and G2 scores

# Make predictions using the loaded model
predicted_grade = loaded_model.predict(student_data)

print(f'Predicted Grade: {predicted_grade[0]}')  # Print the predicted grade


#--------------------------------------------------------------------------------------------------------------


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('student_data.csv')  # Replace with your dataset file
print(data.head())

X = data['study_hours'].values.reshape(-1, 1)  # Independent variable
y = data['exam_scores'].values  # Dependent variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')

plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.legend()
plt.show()
