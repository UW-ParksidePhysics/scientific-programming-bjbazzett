import numpy as np

"""vectorized gaussian function"""
def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

"""vectorized x/y values"""
def main():
    x_values = np.linspace(-4, 4, 41)
    y_values = gaussian(x_values)
    print("Computed Gaussian values:")
    for x, y in zip(x_values, y_values):
        print(f"x = {x:.2f}, g(x) = {y:.5f}")

if __name__ == '__main__':
    main()