"""
fit_curve_array
"""

__author__ = "ben_bazzett"

import numpy as np

def generate_fit_curve(quadratic_coefficients, min_x, max_x, number_of_points=100):
    if max_x < min_x:
        raise ArithmeticError("max_x must be greater than min_x.")
    if number_of_points <= 2:
        raise IndexError("number_of_points has to be above 2.")
    x_values = np.linspace(min_x, max_x, number_of_points)
    p = np.polynomial.Polynomial(quadratic_coefficients)
    y_values = p(x_values)
    return np.array([x_values, y_values])

if __name__ == "__main__":
    coeffs = np.array([0, 0, 1])
    min_x = -2
    max_x = 2
    fit_curve = generate_fit_curve(coeffs, min_x, max_x)
    x_vals = fit_curve[0]
    y_vals = fit_curve[1]
    print("first 5 x-values:", x_vals[:5])
    print("first 5 y-values:", y_vals[:5])
    print("double check y == x^2:", np.allclose(y_vals, x_vals**2))