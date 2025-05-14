"""
calculate_lowest_eigenvectors
"""

__author__ = "ben_bazzett"

import numpy as np

def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    if square_matrix.shape[0] != square_matrix.shape[1]:
        raise ValueError("input has to be a square matrix.")
    if number_of_eigenvectors < 1 or number_of_eigenvectors > square_matrix.shape[0]:
        raise ValueError("invalid number of eigenvectors requested.")
    eigvals, eigvecs = np.linalg.eig(square_matrix)
    sorted_indices = np.argsort(eigvals)
    selected_indices = sorted_indices[:number_of_eigenvectors]
    min_eigenvalues = eigvals[selected_indices]
    min_eigenvectors = eigvecs[:, selected_indices].T
    return min_eigenvalues, min_eigenvectors

if __name__ == "__main__":
    matrix = np.array([[2, -1], [-1, 2]])
    num_vecs = 2
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(matrix, num_vecs)
    print("eigenvalues:", eigenvalues)
    print("eigenvectors:", eigenvectors)