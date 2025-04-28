"""
(feedback) Sundial
make month start marks about 12inch horizontal away from the center line and labeled with the word of the month
set width to 3ft and use angles to set height
mark the solstices and equinoxes with a simple sun icon
mark the perihelion and aphelion with a simple earth icon

note: 4ft/(tan24)=9ft and 4ft/(tan71)=1.4ft so the sundial is about 7.6ft tall and 3ft wide(at widest point). There can be 9 inches or so of space for the height of the sundial past the analemma itself, then 6 inches extra for the wides part of the analemma, making the entire sundial about 10ft tall and 4ft wide.

My goal in this project is to create a sundial based on the analemma of the sun's position in the sky to cast a shadow from the analemma.

import numpy as np
import matplotlib.pyplot as plt


if  __name__ == "__main__":
  azimuths = np.linspace(0, 2*np.pi, 100)
  alitudes = np.sin(azimuths)
  plt.plot(azimuths, alitudes)
  plt.show()
"""
import eot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

e = 0.017
orb_per = 365.25

peri_day = 5
p_degs = 14


axis_norm_degs = 23.5

day_nums = np.arange(1.5, 366.5, 1)

cal_dict = {1: 'January', 32: 'Febuary', 60: 'March', 91: 'April', 182: 'July', 213: 'August'}

cal_dict1 = {3: 'O', 76: '☀️', 171: '☀️', 185: 'O', 266: '☀️', 355: '☀️'}

cal_dict2 = {121: 'May', 152: 'June', 244: 'September', 274: 'October', 305: 'November', 335: 'December'}

scaling_on = True

fig = plt.figure(figsize=(10, 6), num='Equation of Time')
plt.subplots_adjust(top=.925, left=0.100, right=.950, wspace=0.1)
gs = GridSpec(22, 20, figure=fig)

day_nums = np.arange(1.5, 366.5, 1)
min_x, dec_y = eot.analemma_gen(e, p_degs, axis_norm_degs, peri_day, orb_per, day_nums)
ax_analemma = plt.subplot(gs.new_subplotspec((0, 12), colspan=9, rowspan=22))
ax_analemma.set_title("Analemma")
ax_analemma.minorticks_on()
ax_analemma.grid(which='major', linestyle='-', linewidth=0.5, color='grey')
ax_analemma.grid(which='minor', linestyle=':', linewidth=0.5, color='grey')
ax_analemma.set_xlabel('Minutes')
ax_analemma.set_ylabel('Angle')
analemma_line, = ax_analemma.plot(min_x, dec_y, 'k', lw=2)
analemma_ann_list = []

for d, dt_lbl in cal_dict.items():
    ann = ax_analemma.annotate(dt_lbl, (min_x[d - 1], dec_y[d - 1]), textcoords="offset points",
                               xytext=(-40, 0), ha='center', fontsize='small', color='blue',
                               arrowprops=dict(arrowstyle="-", color='black'))
    analemma_ann_list.append(ann)

for d, dt_lbl in cal_dict1.items():
    ann = ax_analemma.annotate(dt_lbl, (min_x[d - 1], dec_y[d - 1]), textcoords="offset points",
                               xytext=(0, 20), ha='center', fontsize='small', color='red',
                               arrowprops=dict(arrowstyle="-", color='black'))
    analemma_ann_list.append(ann)
for d, dt_lbl in cal_dict2.items():
    ann = ax_analemma.annotate(dt_lbl, (min_x[d - 1], dec_y[d - 1]), textcoords="offset points",
                               xytext=(40, 0), ha='center', fontsize='small', color='blue',
                               arrowprops=dict(arrowstyle="-", color='black'))
    analemma_ann_list.append(ann)

def update(val):
    global eot_ann_list, analemma_ann_list

    day_nums = np.arange(1.5, 366.5, 1)
    min_x, dec_y = eot.analemma_gen(e, p_degs, axis_norm_degs, peri_day, orb_per, day_nums)
    analemma_line.set_ydata(dec_y)
    analemma_line.set_xdata(min_x)

plt.show()

#### RENAME from project.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization
