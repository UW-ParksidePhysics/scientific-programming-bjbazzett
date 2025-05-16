import math
import numpy as np
import matplotlib.pyplot as plt

"""returns gauss value for x/g(x)"""
def gaussian(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)

"""adjust positions and sets gaussian value for new positions then plots them"""
if __name__ == '__main__':
    positions = np.linspace(-4, 4, 41)
    gaussian_values = [gaussian(x) for x in positions]
    for x, g in zip(positions, gaussian_values):
        print(f"x = {x:.2f}, g(x) = {g:.5f}")
    plt.figure(figsize=(8, 5))
    plt.plot(positions, gaussian_values, 'b-', marker='o', label=r'$g(x)$')
    plt.title('Gaussian Function $g(x) = \\frac{1}{\\sqrt{2\\pi}} e^{-\\frac{1}{2}x^2}$')
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()