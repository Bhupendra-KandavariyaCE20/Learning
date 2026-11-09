# from src.regression.py import LinearRegressionScratch
import pytest
import numpy as np
from src.regression import LinearRegressionScratch
from sklearn.linear_model import LinearRegression


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


# Multiple feature support
def test_multiple_features():
    # Create a dataset with multiple features
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = 2 * X[:, 0] + 3 * X[:, 1] + 5
    model = LinearRegressionScratch(learning_rate=0.01, epochs=1000)
    model.fit(X, y)

    assert model.weights is not None
    assert model.bias is not None
    assert model.loss_history[-1] < 1e-2  # Ensure the loss is low enough
    prediction = model._predict(np.array([[6, 7]]))
    assert np.isclose(
        prediction[0], 2 * 6 + 3 * 7 + 5, atol=0.1
    )  # Check if prediction is close to the expected value
    assert len(model.loss_history) == 1000  # Ensure the number of epochs is correct


def test_input_validation():
    model = LinearRegressionScratch()
    X = np.array([[1], [2], [3]])
    y = np.array([1, 2])  # Mismatched length

    with pytest.raises(ValueError):
        model.fit(X, y)

    with pytest.raises(ValueError):
        model._predict("not an array")

    model.initialize_parameters(1)
    with pytest.raises(ValueError):
        model._predict(np.array([[1, 2]]))  # Mismatched feature size


def test_against_sklearn():
    # Create a simple linear dataset
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
    y = 3 * X[:, 0] + 2

    # Fit sklearn's LinearRegression
    sklearn_model = LinearRegression()
    sklearn_model.fit(X, y)
    sklearn_predictions = sklearn_model.predict(X)

    # Fit our LinearRegressionScratch
    model = LinearRegressionScratch(learning_rate=0.01, epochs=1000)
    model.fit(X, y)
    scratch_predictions = model._predict(X)

    # Compare predictions
    assert np.allclose(
        sklearn_predictions, scratch_predictions, atol=1e-1
    ), "Predictions from LinearRegressionScratch do not match sklearn's LinearRegression."
