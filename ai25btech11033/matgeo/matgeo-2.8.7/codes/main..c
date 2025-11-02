#include <stdio.h>
#include <math.h>

int main() {
    // Given values
    double a = 2.0;   // |a|
    double b = 3.0;   // |b|
    double dot = 4.0; // a · b

    // Compute cos(theta)
    double cos_theta = dot / (a * b);

    // Compute angle in radians
    double theta_rad = acos(cos_theta);

    // Convert to degrees
    double theta_deg = theta_rad * (180.0 / M_PI);

    // Print results
    printf("cos(theta) = %.2f\n", cos_theta);
    printf("theta (radians) = %.4f\n", theta_rad);
    printf("theta (degrees) = %.2f\n", theta_deg);

    return 0;
}
