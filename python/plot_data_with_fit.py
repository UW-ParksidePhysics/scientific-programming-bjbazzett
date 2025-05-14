"""
plot_data_with_fit
"""

__author__ = "ben_bazzett"

import numpy as np
import matplotlib.pyplot as plt

def plot_with_fit(data, fit_curve, data_format='o', fit_format=''):
    x_data, y_data = data
    x_fit, y_fit = fit_curve
    line_data = plt.plot(x_data, y_data, data_format, label="Data")
    line_fit = plt.plot(x_fit, y_fit, fit_format, label="Fit Curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Data and Quadratic Fit")
    plt.legend()
    return line_data + line_fit

if __name__ == "__main__":
    original_data = np.array([[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]])
    x_vals_fit = np.linspace(-2, 2, 100)
    y_vals_fit = x_vals_fit ** 2
    generated_fit_curve = np.array([x_vals_fit, y_vals_fit])
    combined_plot = plot_with_fit(original_data, generated_fit_curve, data_format='x', fit_format='--')
    plt.show()