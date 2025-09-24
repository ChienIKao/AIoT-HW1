import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Function to generate synthetic data
def generate_data(a=1, b=0, noise=0.1, num_points=100):
    np.random.seed(42)  # For reproducibility
    x = np.linspace(0, 10, num_points)
    y = a * x + b + np.random.normal(0, noise, num_points)
    return x, y

# Function to perform linear regression
def perform_regression(x, y):
    x = x.reshape(-1, 1)  # Reshape for sklearn
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    return model, y_pred, mse, r2

# Streamlit app
st.title("Simple Linear Regression")

# Sidebar for user input
st.sidebar.header("User Input Parameters")
a = st.sidebar.slider("Slope (a)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.sidebar.slider("Intercept (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
noise = st.sidebar.slider("Noise Level", min_value=0.0, max_value=5.0, value=0.1, step=0.1)
num_points = st.sidebar.slider("Number of Points", min_value=10, max_value=500, value=100, step=10)

# Generate data
x, y = generate_data(a, b, noise, num_points)

# Perform regression
model, y_pred, mse, r2 = perform_regression(x, y)

# Display results
st.subheader("Model Results")
st.write(f"Mean Squared Error: {mse}")
st.write(f"R² Score: {r2}")
st.write(f"Model Coefficients: {model.coef_[0]}")
st.write(f"Model Intercept: {model.intercept_}")

# Calculate residuals
residuals = np.abs(y - y_pred)
outlier_indices = np.argsort(residuals)[-5:]  # Indices of top 5 outliers

# Plot results with outliers and annotate coordinates
fig, ax = plt.subplots()
ax.scatter(x, y, label="Data", color="blue")
ax.plot(x, y_pred, label="Regression Line", color="red")
ax.scatter(x[outlier_indices], y[outlier_indices], color="orange", label="Outliers", edgecolor="black", s=100)
for i in outlier_indices:
    ax.annotate(f"({x[i]:.2f}, {y[i]:.2f})", (x[i], y[i]), textcoords="offset points", xytext=(5,5), ha='center')
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Linear Regression with Outliers Highlighted")
st.pyplot(fig)
