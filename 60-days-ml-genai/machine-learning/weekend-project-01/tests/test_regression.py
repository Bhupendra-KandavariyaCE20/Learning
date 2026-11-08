# from src.regression.py import LinearRegressionScratch
import pytest
import numpy as np
from src.regression import LinearRegressionScratch


# check if the LinearRegressionScratch class is defined
def test_linear_regression_scratch_class_exists():
    assert (
        "LinearRegressionScratch" in globals()
    ), "LinearRegressionScratch class is not defined."


def test_linear_relationship():
    # Create a simple linear dataset
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
    y = 3 * X[:, 0] + 2
    model = LinearRegressionScratch(learning_rate=0.01, epochs=1000)
    model.fit(X, y)

    assert model.weights is not None
    assert model.bias is not None
    assert model.loss_history[-1] < 1e-2  # Ensure the loss is low enough
    prediction = model._predict(np.array([[9]]))
    assert np.isclose(
        prediction[0], 29, atol=0.1
    )  # Check if prediction is close to the expected value
    assert np.isclose(
        (model.weights[0] / (model.scale + 1e-8)), 3, atol=0.1
    )  # Check if the learned weight is close to the expected value
