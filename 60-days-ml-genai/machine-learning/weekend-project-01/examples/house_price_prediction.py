import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from src.regression import LinearRegressionScratch
from sklearn.linear_model import LinearRegression

df = pd.read_csv("examples/house_prices.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df.drop(columns=["house_size_sq_ft"]),
    df["price_in_lakh_inr"],
    test_size=0.2,
    random_state=42,
)


def evaluate_model(model, X_test, y_test):
    y_pred = model._predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse**0.5
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-squared (R2): {r2:.4f}")


# X and y should be numpy arrays for the LinearRegressionScratch model
scratch_model = LinearRegressionScratch(learning_rate=0.01, epochs=1000).fit(
    X_train.to_numpy(), y_train.to_numpy()
)
sklearn_model = LinearRegression().fit(X_train, y_train)
evaluate_model(
    scratch_model,
    X_test.to_numpy(),
    y_test.to_numpy(),
)
evaluate_model(sklearn_model, X_test, y_test)

import matplotlib.pyplot as plt

plt.plot(scratch_model.loss_history)

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Gradient Descent Convergence")

plt.grid(True)
plt.show()
