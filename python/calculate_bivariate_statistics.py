"""
calculate_bivaraiate_stastics
"""

__author__ = "ben_bazzett"

import numpy as np
from scipy import stats

def calculate_bivariate_statistics(data):
    if data.shape[0] != 2 or data.shape[1] <= 1:
        raise IndexError("Input must have shape (2, M) with M > 1.")
    x_values = data[0]
    y_values = data[1]
    y_stats = stats.describe(y_values)
    mean_y = y_stats.mean
    std_y = np.sqrt(y_stats.variance)
    min_x = np.min(x_values)
    max_x = np.max(x_values)
    min_y = np.min(y_values)
    max_y = np.max(y_values)
    return np.array([mean_y, std_y, min_x, max_x, min_y, max_y])

if __name__ == '__main__':
    x = np.linspace(-10, 10, 100)
    y = x ** 2
    data_test = np.vstack((x, y))
    statistics = calculate_bivariate_statistics(data_test)
    labels = ['mean(y)', 'std(y)', 'min(x)', 'max(x)', 'min(y)', 'max(y)']
    print("bivariate statistics:")
    for label, value in zip(labels, statistics):
        print(f"{label}: {value:.4f}")