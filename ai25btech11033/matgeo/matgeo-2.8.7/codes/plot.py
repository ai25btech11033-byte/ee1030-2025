import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the points
A = np.array([-1, 0, -2])
B = np.array([0, 2, 1])
C = np.array([-1, 4, 1])

# Calculate vectors AB and AC
AB = B - A
AC = C - A

# Cross product
cross_prod = np.cross(AB, AC)

# Area of the triangle
area = 0.5 * np.linalg.norm(cross_prod)
print(f"Area of the triangle: {area:.4f}")

# Plotting the triangle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vertices
ax.scatter(*A, color='r', label='A (-1,0,-2)')
ax.scatter(*B, color='g', label='B (0,2,1)')
ax.scatter(*C, color='b', label='C (-1,4,1)')

# Draw the edges of the triangle
triangle = Poly3DCollection([ [A, B, C] ], alpha=0.5, facecolor='cyan')
ax.add_collection3d(triangle)

# Label points
ax.text(*A, "A", color='red')
ax.text(*B, "B", color='green')
ax.text(*C, "C", color='blue')

# Set axes labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Set equal aspect ratio for all axes
max_range = np.array([A, B, C]).ptp(axis=0).max() / 2.0

mid_x = (A[0] + B[0] + C[0]) / 3
mid_y = (A[1] + B[1] + C[1]) / 3
mid_z = (A[2] + B[2] + C[2]) / 3

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

ax.legend()
ax.set_title("Triangle with vertices A, B, C")

plt.show()

