import numpy as np
from numpy.typing import NDArray

# class LinearRegressionScratch:
#     def __init__(self, learning_rate, epochs):


class LinearRegressionScratch:
    def __init__(self, learning_rate: float = 0.01, epochs: int = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.weights = None
        self.bias = None

        self.mean = None
        self.scale = None

        self.loss_history = []

    def initialize_parameters(self, n_features: int) -> None:
        self.weights = np.zeros(n_features)
        self.bias = 0.0

    def _predict(self, x: np.ndarray) -> np.ndarray:
        # Validate the input
        self._validate_predict_input(x)
        x_scaled = self.standardize(x, fit=False)
        return np.dot(x_scaled, self.weights) + self.bias

    def _compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        return np.mean((y_pred - y_true) ** 2)

    def _compute_gradients(
        self, X: np.ndarray, y_true: np.ndarray, y_pred: np.ndarray
    ) -> tuple[np.ndarray, float]:
        dj_dw = 2 / X.shape[0] * (np.dot(np.transpose(X), y_pred - y_true))
        dj_db = 2 / X.shape[0] * np.sum(y_pred - y_true)
        return dj_dw, dj_db

    def _update_parameters(self, dw: np.ndarray, db: float) -> None:
        self.weights = self.weights - self.learning_rate * dw
        self.bias = self.bias - self.learning_rate * db

    def standardize(self, X: np.ndarray, fit: bool) -> np.ndarray:
        if fit:
            self.mean = np.mean(X, axis=0)
            self.scale = np.std(X, axis=0)
        return (X - self.mean) / (
            self.scale + 1e-8
        )  # Add a small value to avoid division by zero

    def _validate_input(self, X: np.ndarray, y: np.ndarray) -> None:
        if not isinstance(X, np.ndarray) or not isinstance(y, np.ndarray):
            raise ValueError("X and y must be numpy arrays.")
        if X.shape[0] != y.shape[0]:
            raise ValueError("The number of samples in X and y must be the same.")

    def _validate_predict_input(self, X: np.ndarray) -> None:
        if not isinstance(X, np.ndarray):
            raise ValueError("X must be a numpy array.")
        if self.weights is None or self.bias is None:
            raise ValueError(
                "Model parameters are not initialized. Fit the model first."
            )
        if X.shape[1] != self.weights.shape[0]:
            raise ValueError(
                f"Number of features in X ({X.shape[1]}) does not match number of weights ({self.weights.shape[0]})."
            )

    def fit(self, X: np.ndarray, y: np.ndarray):
        # Validate the training data
        self._validate_input(X, y)

        # Initialize parameters
        self.initialize_parameters(X.shape[1])

        self.standardize(X, fit=True)

        # Train the model
        for epoch in range(self.epochs):
            # Make predictions
            y_pred = self._predict(X)

            # Compute loss
            loss = self._compute_loss(y, y_pred)
            self.loss_history.append(loss)

            # Compute gradients
            X_scaled = self.standardize(X, fit=False)
            dw, db = self._compute_gradients(X_scaled, y, y_pred)

            # Update parameters
            self._update_parameters(dw, db)
