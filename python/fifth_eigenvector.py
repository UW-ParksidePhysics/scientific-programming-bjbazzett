import numpy as np
import matplotlib.pyplot as plt

"""create and format the matrix"""
n = 5
h = 1 / (n + 1)
main_diag = 2 * np.ones(n)
off_diag = -1 * np.ones(n - 1)
H = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
H *= 1 / (2 * h**2)

"""compute/sort vectors"""
eigenvalues, eigenvectors = np.linalg.eig(H)
idx = np.argsort(eigenvalues)
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]
fifth_eigenvector = eigenvectors[:, 4]

"""set/normalize the vectors"""
x_values = np.linspace(h, 1 - h, n)
sine_values = np.sqrt(2) * np.sin(np.pi * x_values)
fifth_eigenvector_normalized = fifth_eigenvector / np.linalg.norm(fifth_eigenvector) * np.linalg.norm(sine_values)

"""plot"""
plt.plot(x_values, fifth_eigenvector_normalized, 'o-', label='5th Eigenvector')
plt.plot(x_values, sine_values, '--', label=r'$\sqrt{2} \sin(\pi x)$')
plt.xlabel('x')
plt.ylabel('Function value')
plt.title(r'Comparison of 5th Eigenvector and $\sqrt{2} \sin(\pi x)$')
plt.legend()
plt.grid(True)
plt.show()