"""
My goal in this project is to design a 7.6ft x 3ft analemma on the ground that mirrors the sun's own analemma to cast a
shadow on a series of yet-to-be-designed marker stones, the central point of which will be a midday marker stone 1.6ft
past the most upward tip of the ground-analemma. The overall design and size of the analemma has been adjusted for a
4ft tall individual, sized for visiting students, but also with the intent that it does not need to be 100% accurate to
function properly, allowing visitors to approximate the day while still having their shadow roughly line up with the
sundial. For this purpose the months have been marked alone the 'route' so that guests can approximate the date
corresponding to their spot on the analemma. For purposes of learning the equinoxes, solstices, and ap/peri-helions have
been marked with astronomical symbols as well.
"""
import eot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

eccentricity = 0.017
rotation_period = 365.25

perihelion_date = 5
perihelion_degs = 14

axis_variation = 23.5

day = np.arange(1.5, 367.5, 1)

left_months = {1: 'January', 32: 'February', 60: 'March', 91: 'April', 182: 'July', 213: 'August'}

equinoxes_solstices_helions = {3: '\u2295', 76: '♈', 171: '♋︎', 185: '\u2295', 266: '♎︎', 355: '♑︎'}

right_months = {121: 'May', 152: 'June', 244: 'September', 274: 'October', 305: 'November', 335: 'December'}

scaling_on = True

fig = plt.figure(figsize=(10, 6), num='Equation of Time')
gs = GridSpec(20, 20, figure=fig)

min_x, dec_y = eot.analemma_gen(eccentricity, perihelion_degs, axis_variation, perihelion_date, rotation_period, day)
ax_analemma = plt.subplot(gs.new_subplotspec((0, 3), colspan=15, rowspan=22))
ax_analemma.set_title("Analemma")
ax_analemma.minorticks_on()
ax_analemma.grid(which='major', linestyle='-', linewidth=0.5, color='grey')
ax_analemma.grid(which='minor', linestyle=':', linewidth=0.5, color='grey')
ax_analemma.set_xlabel('Inches')
ax_analemma.set_ylabel('Inches')
analemma_line, = ax_analemma.plot(min_x, dec_y, 'k', lw=2)
analemma_ann_list = []

for d, dt_lbl in left_months.items():
    ann = ax_analemma.annotate(dt_lbl, (min_x[d - 1], dec_y[d - 1]), textcoords="offset points",
                               xytext=(-155, -2.5), ha='center', fontsize='small', color='blue',
                               arrowprops=dict(arrowstyle="-", color='black'))
    analemma_ann_list.append(ann)

for d, dt_lbl in equinoxes_solstices_helions.items():
    ann = ax_analemma.annotate(dt_lbl, (min_x[d - 1], dec_y[d - 1]), textcoords="offset points",
                               xytext=(0, -10), ha='center', fontsize='30', color='red',
                               arrowprops=dict(arrowstyle="-", color='black'))
    analemma_ann_list.append(ann)
for d, dt_lbl in right_months.items():
    ann = ax_analemma.annotate(dt_lbl, (min_x[d - 1], dec_y[d - 1]), textcoords="offset points",
                               xytext=(155, -2.5), ha='center', fontsize='small', color='blue',
                               arrowprops=dict(arrowstyle="-", color='black'))
    analemma_ann_list.append(ann)

def update(val):
    global eot_ann_list, analemma_ann_list

    days = np.arange(1.5, 367.5, 1)
    min_x, dec_y = eot.analemma_gen(eccentricity, day, axis_variation, perihelion_date, rotation_period, days)
    analemma_line.set_ydata(dec_y)
    analemma_line.set_xdata(min_x)

plt.show()