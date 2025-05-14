"""
calculate_quadratic_fit
"""

__author__ = "ben_bazzett"

import numpy as np

def fit_quadratic(nparray):
    x = nparray[0]
    y = nparray[1]
    coeffs = np.polyfit(x, y, deg=2)
    return coeffs[::-1]

if __name__ == "__main__":
    x_val = np.linspace(-1, 1)
    y_val = x_val ** 2
    shape = np.array([x_val, y_val])

    coeffs = fit_quadratic(shape)
    print("fitted coefficients (constant, linear, quadratic):", coeffs)