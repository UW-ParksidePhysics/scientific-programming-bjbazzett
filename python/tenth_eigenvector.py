import numpy as np
import matplotlib.pyplot as plt

"""matrix dimensions/step size"""
matrix_dimension = 10
h = 1 / (matrix_dimension + 1)

"""construct matrix"""
diagonal = 2 * np.ones(matrix_dimension)
off_diagonal = -1 * np.ones(matrix_dimension - 1)
H = np.diagflat(diagonal) + np.diagflat(off_diagonal, -1) + np.diagflat(off_diagonal, 1)
H *= 1 / (2 * h**2)

"""compute and sort eigen values"""
eigenvalues, eigenvectors = np.linalg.eig(H)
indices = np.argsort(eigenvalues)
eigenvectors = eigenvectors[:, indices]

"""get eigenvectors, normalize, and function to comp"""
target_index = matrix_dimension - 1
target_vector = eigenvectors[:, target_index]
target_vector = target_vector / np.max(np.abs(target_vector))
x_values = np.linspace(h, 1 - h, matrix_dimension)
analytic_function = np.sqrt(2) * np.sin(matrix_dimension * np.pi * x_values)

"""plot eigenvectors"""
plt.figure(figsize=(8, 5))
plt.plot(x_values, target_vector, 'o-', label=f'{matrix_dimension}th Eigenvector (numerical)')
plt.plot(x_values, analytic_function, 'r--', label=fr'$\sqrt{{2}} \sin({matrix_dimension} \pi x)$')
plt.xlabel('x')
plt.ylabel('Amplitude')
plt.title(rf'Comparison of {matrix_dimension}th Eigenvector and $\sqrt{{2}} \sin({matrix_dimension} \pi x)$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()