"""Generate Hertzsprung-Russell diagram like:
    https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram#/media/File:HRDiagram.png"""
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

astronomical_unit = 1.495978707e11  # meters
meters_to_light_years = 1./9.4607e15

def star_colormap(star_b_minus_vs):
    # Create color map from B-V = -0.33 (#7070ff) to 1.40 (#ff7f7f)
    # yellow = #ffff7f at B-V = 0.81
    number_of_gradient_points = 256
    white_index = int((0.33 / (0.33 + 1.40)) * number_of_gradient_points)
    yellow_index = int(((0.81 + .33) / (0.33 + 1.40)) * number_of_gradient_points)
    color_values = np.ones((number_of_gradient_points, 4))
    color_values[:white_index, 0] = np.linspace(112 / 255, 255 / 255, white_index)
    color_values[white_index:yellow_index, 0] = 1
    color_values[yellow_index:, 0] = 1
    color_values[:white_index, 1] = np.linspace(112 / 255, 255 / 255, white_index)
    color_values[white_index:yellow_index, 1] = 1
    color_values[yellow_index:, 1] = np.linspace(255 / 255, 127 / 255, number_of_gradient_points - yellow_index)
    color_values[:white_index, 2] = 1
    color_values[white_index:yellow_index, 2] = np.linspace(255 / 255, 127 / 255, yellow_index - white_index)
    color_values[yellow_index:, 2] = 127 / 255

    new_colormap = ListedColormap(color_values)
    scaled_b_minus_vs = (star_b_minus_vs - np.amin(star_b_minus_vs)) / (
            np.amax(star_b_minus_vs) - np.amin(star_b_minus_vs))

    return scaled_b_minus_vs, new_colormap


def parallax_to_distance(parallax):
    """Take parallax in milliarcseconds and convert to distance in meters"""
    parallax_in_radians = (parallax / 1000. / 3600.) * (2 * np.pi / 360.)
    distance = astronomical_unit / np.tan(parallax_in_radians)
    return distance


def apparent_to_absolute_magnitude(apparent_magnitude, distance):
    """Calculate absolute magnitude from apparent magnitude and distance in meters"""
    distance_in_parsecs = distance / (648000. * astronomical_unit / np.pi)
    absolute_magnitude = apparent_magnitude - 5 * np.log10(distance_in_parsecs) + 5
    return absolute_magnitude


def read_file(filename):
    """Read four column data from HIPPARCOS satellite and return a nested dictionary"""
    hipparcos_data = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                parts = line.strip().split()
                catalog_id = int(parts[0])
                parallax = float(parts[1])
                apparent_mag = float(parts[2])
                b_minus_v = float(parts[3])
                hipparcos_data[catalog_id] = {
                    'parallax': parallax,
                    'apparent_magnitude': apparent_mag,
                    'blue_minus_visual': b_minus_v
                }
    return hipparcos_data

if __name__ == '__main__':
  # Apply read function to the data file and produce a nested dictionary
  hipparcos_dictionary = read_file('hipparcos_data.txt')

  star_b_minus_vs = []
  star_absolute_magnitudes = []
  for star in hipparcos_dictionary.values():
      parallax = star['parallax']
      if parallax > 0:
          distance = parallax_to_distance(parallax)
          absolute_mag = apparent_to_absolute_magnitude(star['apparent_magnitude'], distance)
          star_absolute_magnitudes.append(absolute_mag)
          star_b_minus_vs.append(star['blue_minus_visual'])
  plt.style.use('dark_background')

  star_b_minus_vs = np.array(star_b_minus_vs)
  star_absolute_magnitudes = np.array(star_absolute_magnitudes)
  # Reverse the absolute magnitude so that negative values appear on top
  plt.style.use('dark_background')
  star_absolute_magnitudes = -star_absolute_magnitudes
  
  # Get color map to match star colors
  scaled_b_minus_v, hr_colormap = star_colormap(star_b_minus_vs)
  
  # Create axes labels
  # Make the axes identical to the model figure referenced at the top of this file
  plt.figure(figsize=(10, 8))
  plt.scatter(star_b_minus_vs, star_absolute_magnitudes, c=scaled_b_minus_v, cmap=hr_colormap, s=10)
  plt.xlabel('B−V Color Index')
  plt.ylabel('Absolute Magnitude (inverted)')
  plt.title('Hertzsprung-Russell Diagram')
  plt.xlim(-0.5, 2.0)
  plt.ylim(-20, 5)
  plt.grid(True, linestyle=':', linewidth=0.5)

  # Define the scatter marker size in points squared (make it similar to the model figure)
  plt.text(-0.45, -21, "Created by (ben)", fontsize=10, ha='left', va='top')

  plt.tight_layout()
  plt.savefig("hertzsprung_russell_diagram.png", dpi=300)
  plt.show()
