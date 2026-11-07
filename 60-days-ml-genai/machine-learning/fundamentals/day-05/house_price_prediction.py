import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    root_mean_squared_error,
    r2_score,
)

# Load the dataset
df = pd.read_csv("house_prices.csv")
print(df.head(2))

# Separate features and target variable
X = df[["house_size_sq_ft"]]
y = df["price_in_lakh_inr"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize the Linear Regression model
model = LinearRegression()

# Fit the model on x_train and y_train
model.fit(X_train, y_train)

# Predict using predict()
y_predicted = model.predict(X_test)

print(f"Coeff {model.coef_}")


print(f"Intercept {model.intercept_}")
# coef_[0] represents \(w\).
# intercept_ represents \(b\).
print(f"MSE {mean_squared_error(y_test, y_predicted)}")
print(f"RMSE {root_mean_squared_error(y_test, y_predicted)}")
print(f"MAE {mean_absolute_error(y_test, y_predicted)}")
print(f"R^2 {r2_score(y_test, y_predicted)}")

new_house = pd.DataFrame({"house_size_sq_ft": [1750]})
print(f"New House Price {model.predict(new_house)}")

# Visualize predictions
