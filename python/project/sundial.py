"""
(feedback) Sundial
make month start marks about 12inch horizontal away from the center line and labeled with the word of the month
set width to 3ft and use angles to set height
mark the solstices and equinoxes with a simple sun icon
mark the perihelion and aphelion with a simple earth icon

note: 4ft/(tan24)=9ft and 4ft/(tan71)=1.4ft so the sundial is about 7.6ft tall and 3ft wide
"""

import numpy as np
import matplotlib.pyplot as plt


if  __name__ == "__main__":
  azimuths = np.linspace(0, 2*np.pi, 100)
  alitudes = np.sin(azimuths)
  plt.plot(azimuths, alitudes)
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
