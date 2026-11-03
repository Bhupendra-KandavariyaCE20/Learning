import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

print("----------------------------------")
print("   Basic Operations")
print(f"Addition: {vector_a+vector_b}")
print(f"Substraction: {vector_b-vector_a}")
print(f"Multiplication: {vector_a*vector_b}")
print(f"Scaler: {vector_a*2}")


print("\n\n----------------------------------")
print(f"Dot Product: {np.dot(vector_a, vector_b)}")


print("\n\n----------------------------------")
matrix_a = np.array([[5, 6], [3, 5]])
print(f"Matrix_a shape {matrix_a.shape}")

matrix_b = np.array([[1, 2], [3, 4]])
print(f"Matrix_b shape {matrix_b.shape}")

print("Addition:")
print(matrix_a + matrix_b)

print("Substraction")
print(matrix_a - matrix_b)

print("Multiplication")
print(np.dot(matrix_a, matrix_b))
# print(matrix_a@matrix_b)  # This is equivalent to np.dot(matrix_a, matrix_b)

print("Transpose:")
print(matrix_a.T)
