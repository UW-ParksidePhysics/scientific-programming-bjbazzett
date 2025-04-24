"""
testing astropy
"""""
import numpy as np
from astropy.time import Time
from astropy.coordinates import get_sun
import matplotlib.pyplot as plt
start_date = ('2024-01-01')
end_date = ('2024-12-31')
date_range = (np.linspace(start_date.mjd, end_date.mjd, 365))
# Import astropy library 
import astropy
sun_position = astropy.Time(date_range, format='mjd')
ra_dec = sun_position.ra, sun_position.dec
plt.figure(figsize=(7.6, 3))
plt.plot(ra_dec[0].degree, ra_dec[1].degree, marker='o', linestyle='-', color='b')
plt.xlabel('Right Ascension (degrees)')
plt.ylabel('Declination (degrees)')
plt.title('Analemma')
plt.grid(True)
plt.show()