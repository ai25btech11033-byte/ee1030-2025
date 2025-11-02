import math

# Given values
a = 2.0   # |a|
b = 3.0   # |b|
dot = 4.0 # a · b

# Compute cos(theta)
cos_theta = dot / (a * b)

# Compute angle in radians
theta_rad = math.acos(cos_theta)

# Convert to degrees
theta_deg = math.degrees(theta_rad)

# Print results
print("cos(theta) =", round(cos_theta, 2))
print("theta (radians) =", round(theta_rad, 4))
print("theta (degrees) =", round(theta_deg, 2))
