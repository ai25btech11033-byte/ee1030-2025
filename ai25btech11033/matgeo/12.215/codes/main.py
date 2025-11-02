import numpy as np

# Define the matrix A
A = np.array([
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 1]
])

# Compute the inverse of A
A_inv = np.linalg.inv(A)

# Display the matrix and its inverse
print("Matrix A:")
print(A)

print("\nInverse of A:")
print(A_inv)

# Verify that A * A_inv = I
I = np.dot(A, A_inv)

print("\nVerification (A * A_inv):")
print(I)

