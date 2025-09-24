import numpy as np
import pandas as pd
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

# Example usage
def main():
    # User-defined parameters
    a = float(input("Enter the slope (a) for y = ax + b: "))
    b = float(input("Enter the intercept (b) for y = ax + b: "))
    noise = float(input("Enter the noise level: "))
    num_points = int(input("Enter the number of data points: "))

    # Generate data
    x, y = generate_data(a, b, noise, num_points)

    # Perform regression
    model, y_pred, mse, r2 = perform_regression(x, y)

    # Display results
    print(f"Mean Squared Error: {mse}")
    print(f"R² Score: {r2}")
    print(f"Model Coefficients: {model.coef_}")
    print(f"Model Intercept: {model.intercept_}")

    # Plot results
    plt.scatter(x, y, label="Data", color="blue")
    plt.plot(x, y_pred, label="Regression Line", color="red")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Regression")
    plt.show()

if __name__ == "__main__":
    main()
