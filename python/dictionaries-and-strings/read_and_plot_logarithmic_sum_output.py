import re
import matplotlib.pyplot as plt

def parse_sum_output(filename):
    tolerances = []
    errors = []
    max_indices = []
    with open(filename, 'r') as file:
        for line in file:
            if 'epsilon' in line and 'exact error' in line:
                match = re.search(
                    r'epsilon:\s*([\deE\.-]+),\s*exact error:\s*([\deE\.-]+),\s*n=(\d+)', line)
                if match:
                    epsilon = float(match.group(1))
                    error = float(match.group(2))
                    n = int(match.group(3))
                    tolerances.append(epsilon)
                    errors.append(error)
                    max_indices.append(n)
    return tolerances, errors, max_indices

def plot_logarithmic_sum_error(tolerances, errors, max_indices):
    plt.figure(figsize=(8, 6))
    plt.semilogy(max_indices, tolerances, 'o-', label=r'$\varepsilon$ (tolerance)', color='blue')
    plt.semilogy(max_indices, errors, 's--', label=r'$\Delta$ (exact error)', color='red')
    plt.xlabel('n (number of terms)')
    plt.ylabel('Log scale: ε and Δ')
    plt.title('Epsilon and Approximation Error vs n')
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.legend()
    for x, y in zip(max_indices, tolerances):
        plt.annotate(f"{x}", (x, y), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8, color='blue')
    for x, y in zip(max_indices, errors):
        plt.annotate(f"{x}", (x, y), textcoords="offset points", xytext=(0, -10), ha='center', fontsize=8, color='red')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    tolerances, errors, max_indices = parse_sum_output('logarithmic_sum.out')
    print("Parsed Data:")
    for eps, err, n in zip(tolerances, errors, max_indices):
        print(f"epsilon: {eps:.1e}, error: {err:.2e}, n: {n}")
    plot_logarithmic_sum_error(tolerances, errors, max_indices)