import numpy as np
import matplotlib.pyplot as plt

astronomical_unit = 1.495978707e11

def parallax_to_distance(parallax_mas):
    radians = (parallax_mas / 1000.0 / 3600.0) * (2 * np.pi / 360.0)
    return astronomical_unit / np.tan(radians)

def apparent_to_absolute_magnitude(apparent_mag, distance_m):
    parsec = distance_m / (648000. * astronomical_unit / np.pi)
    return apparent_mag - 5 * np.log10(parsec) + 5

def read_file(filename):
    star_data = {}
    with open(filename) as file:
        file.readline()  # skip header
        for line in file:
            if len(line.split()) != 4:
                continue
            hip, parallax, mag, bv = line.split()
            star_data[int(hip)] = {
                'parallax': float(parallax),
                'apparent_magnitude': float(mag),
                'b_minus_v': float(bv)
            }
    return star_data

def star_colormap(bv_values):
    colors = plt.cm.plasma
    scaled = (bv_values - np.min(bv_values)) / (np.max(bv_values) - np.min(bv_values))
    return scaled, colors

def label_bright_stars(ax, star_dict):
    star_names = {
        32349: "Sirius",
        30438: "Canopus",
        69673: "Arcturus",
        71683: "Alpha Centauri A",
        91262: "Vega",
        0: "Sun"
    }
    for hip, name in star_names.items():
        if hip == 0:
            bv = 0.65
            abs_mag = 4.83
        else:
            entry = star_dict.get(hip)
            if not entry: continue
            dist = parallax_to_distance(entry['parallax'])
            abs_mag = apparent_to_absolute_magnitude(entry['apparent_magnitude'], dist)
            bv = entry['b_minus_v']
        ax.annotate(name, (bv, -abs_mag), fontsize=9, color='white', ha='left', va='center')

def add_luminosity_axis(ax):
    mag_ticks = np.arange(-10, 20, 2)
    lum_ticks = 10 ** ((4.83 - mag_ticks) / 2.5)
    ax2 = ax.twinx()
    ax2.set_yticks(mag_ticks)
    ax2.set_yticklabels([f"{l:.2f}" for l in lum_ticks])
    ax2.set_ylabel("Luminosity [L☉]", color='white')
    ax2.tick_params(axis='y', colors='white')

def add_temperature_axis(ax):
    ax_top = ax.twiny()
    temp_labels = ['30000', '10000', '7500', '6000', '5000', '4000', '3000']
    bv_ticks = [-0.3, 0.0, 0.3, 0.6, 0.9, 1.2, 1.5]
    ax_top.set_xlim(ax.get_xlim())
    ax_top.set_xticks(bv_ticks)
    ax_top.set_xticklabels(temp_labels)
    ax_top.set_xlabel("Temperature [K]", color='white')
    ax_top.tick_params(axis='x', colors='white')

if __name__ == '__main__':
    data = read_file("hipparcos_data.txt")
    bv_values, abs_mags = [], []
    for entry in data.values():
        dist = parallax_to_distance(entry['parallax'])
        abs_mag = apparent_to_absolute_magnitude(entry['apparent_magnitude'], dist)
        abs_mags.append(abs_mag)
        bv_values.append(entry['b_minus_v'])
    bv_values = np.array(bv_values)
    abs_mags = np.array(abs_mags)
    abs_mags = -abs_mags  # invert for HR plot
    scaled_bv, cmap = star_colormap(bv_values)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 8))
    scatter = ax.scatter(bv_values, abs_mags, c=scaled_bv, cmap=cmap, s=2, alpha=0.6)
    ax.set_xlabel("Color Index (B−V)")
    ax.set_ylabel("Absolute Magnitude")
    ax.set_title("Hertzsprung-Russell Diagram")
    ax.set_xlim(-0.4, 2.0)
    ax.set_ylim(20, -10)
    plt.text(-0.35, 21, "Created by (ben)", ha='left', va='top', fontsize=10, color='gray')
    label_bright_stars(ax, data)
    add_luminosity_axis(ax)
    add_temperature_axis(ax)
    plt.tight_layout()
    plt.savefig("hertzsprung_russell_diagram.png", dpi=300)
    plt.show()