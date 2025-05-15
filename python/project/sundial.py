"""
My goal in this project is to design a 7.6ft x 3ft analemma on the ground that mirrors the sun's own analemma to cast a
shadow on a series of yet-to-be-designed marker stones, the central point of which will be a midday marker stone 1.6ft
past the most upward tip of the ground-analemma. The overall design and size of the analemma has been adjusted for a
4ft tall individual, sized for visiting students, but also with the intent that it does not need to be 100% accurate to
function properly, allowing visitors to approximate the day while still having their shadow roughly line up with the
sundial. For this purpose the months have been marked along the 'route' so that guests can approximate the date
corresponding to their spot on the analemma. For purposes of learning the equinoxes, solstices, and ap/peri-helions have
been marked with astronomical symbols as well.
"""
import eot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Astronomical parameters
eccentricity = 0.017
rotation_period_days = 365.25
perihelion_day = 5
perihelion_longitude_deg = 14
axial_tilt_deg = 23.5
days = np.arange(1.5, 367.5, 1)

# Month labels and astronomical symbols for annotation
left_months = {1: 'January', 32: 'February', 60: 'March', 91: 'April', 182: 'July', 213: 'August'}
right_months = {121: 'May', 152: 'June', 244: 'September', 274: 'October', 305: 'November', 335: 'December'}
special_symbols = {3: '\u2295', 76: '♈', 171: '♋︎', 185: '\u2295', 266: '♎︎', 355: '♑︎'}

"""
Adds a labeled annotation to a plot at a specified data point, with parameters;
(ax, x, y, label, offset, color, fontsize)
with returns being matplotlib.text.annotation
"""
def annotate(ax, x, y, label, offset, color, fontsize):
    return ax.annotate(
        label, (x, y),
        textcoords="offset points",
        xytext=offset,
        ha='center',
        fontsize=fontsize,
        color=color,
        arrowprops=dict(arrowstyle="-", color='black')
    )

"""
Plots and creates the analemma via EoT and declination, with parameters;
(eot in mins, declination degrees{both adjusted both ratios to inches})
with return tuple based on fig,ax, line(created obj, subplot axis, lines representing curve)
"""
def plot_analemma(equation_of_time_minutes, declination_degrees):

    fig = plt.figure(figsize=(10, 6), num='Equation of Time')
    grid_spec = GridSpec(20, 20, figure=fig)
    ax = fig.add_subplot(grid_spec.new_subplotspec((0, 3), colspan=15, rowspan=22))

    ax.set_title("Analemma")
    ax.set_xlabel('Inches')
    ax.set_ylabel('Inches')
    ax.minorticks_on()
    ax.set_aspect('equal', adjustable='datalim')
    ax.grid(which='major', linestyle='-', linewidth=0.5, color='grey')
    ax.grid(which='minor', linestyle=':', linewidth=0.5, color='grey')

    # Plot the analemma curve
    line, = ax.plot(equation_of_time_minutes, declination_degrees, 'k', lw=2)

    # Add month and symbol annotations
    for day, label in left_months.items():
        annotate(ax, equation_of_time_minutes[day - 1], declination_degrees[day - 1],
                 label, offset=(-63, -2.5), color='blue', fontsize='small')
    for day, symbol in special_symbols.items():
        annotate(ax, equation_of_time_minutes[day - 1], declination_degrees[day - 1],
                 symbol, offset=(0, -10), color='red', fontsize=30)
    for day, label in right_months.items():
        annotate(ax, equation_of_time_minutes[day - 1], declination_degrees[day - 1],
                 label, offset=(63, -2.5), color='blue', fontsize='small')
    return fig, ax, line

"""
Main function to generate and plot the analemma
"""
def main():
    equation_of_time_minutes, declination_degrees = eot.generate_analemma(
        eccentricity,
        perihelion_longitude_deg,
        axial_tilt_deg,
        perihelion_day,
        rotation_period_days,
        days
    )
    plot_analemma(equation_of_time_minutes, declination_degrees)
    plt.show()

if __name__ == '__main__':
    main()