import sys
import numpy as np
import matplotlib.pyplot as plt

"""computes the vertical position based on time"""
def y_trajectory(t, v0, g):
    return v0 * t - 0.5 * g * t ** 2

"""grav acceleration and initial velocities from the command line are plotted for each initial vel in range"""
def main():
    if len(sys.argv) < 3:
        print("Usage: python projectile_plot.py <g> <v0_1> <v0_2> ... <v0_n>")
        return
    try:
        g = float(sys.argv[1])
        v0_values = [float(v) for v in sys.argv[2:]]
    except ValueError:
        print("All arguments must be numeric.")
        return
    plt.figure(figsize=(8, 6))
    for v0 in v0_values:
        t_max = 2 * v0 / g
        t_values = np.linspace(0, t_max, 100)
        y_values = y_trajectory(t_values, v0, g)
        plt.plot(t_values, y_values, label=f"$v_0 = {v0}$")
    plt.title("Projectile Motion for Various $v_0$ Values")
    plt.xlabel("Time (s)")
    plt.ylabel("Height y(t) (m)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()