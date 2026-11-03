import numpy as np

X = np.array(
    [
        [1000, 2],
        [1500, 3],
        [2000, 4],
        [1200, 2],
        [1800, 3],
    ]
)

weights = np.array([[0.04], [5]])

bias = 10


# validate if shape are compatible for dot product
if X.shape[1] != weights.shape[0]:
    raise ValueError(
        f"Shape mismatch: X has shape {X.shape} and weights has shape {weights.shape}. "
        "The number of columns in X must match the number of rows in weights for dot product."
    )


# TODO: Implement prediction calculation
y = np.dot(X, weights) + bias

print(y)
print(type(y))  # Check the type of y
