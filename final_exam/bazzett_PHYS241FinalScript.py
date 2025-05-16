import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from python.read_two_columns_text import read_two_column_data
from python.calculate_bivariate_statistics import calculate_bivariate_statistics
from python.calculate_quadratic_fit import fit_quadratic
from equations_of_state import fit_equation_of_state
from generate_matrix import generate_matrix
from python.calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from python.annotate_plot import annotate_plot

def convert_units(value, from_units, to_units):
    factors = {
        ('cubic_bohr', 'cubic_angstrom'): 0.14818471147216278,
        ('rydberg', 'eV'): 13.605693122994,
        ('rydberg_per_cubic_bohr', 'GPa'): 14710.507848260711}
    return value * factors[(from_units, to_units)]

def annotate(ax, entries):
    today = datetime.today().date().isoformat()
    annotation = {
        f"Created by (ben) (bazzett) ({today})": {'position': [0.01, 0.01], 'alignment': ['left', 'bottom'], 'fontsize': 10}}
    annotation.update(entries)
    annotate_plot(annotation)

def analyze(filename, display_graph=False):
    parts = filename.split('.')
    chem, symmetry, approx = parts[1], parts[2], parts[3]
    data = read_two_column_data(filename)
    if symmetry == "Fd-3m":
        data[1] /= 2
    stats = calculate_bivariate_statistics(data)
    coeffs = fit_quadratic(data)
    eq_vol_guess = -coeffs[1] / (2 * coeffs[2])
    if eq_vol_guess <= 0:
        raise ValueError("Invalid equilibrium volume")
    data[0] = np.clip(data[0], 1e-6, None)
    eos_curve, eos_params = fit_equation_of_state(data[0], data[1], coeffs, equation_of_state='birch-murnaghan')
    eq_vol = convert_units(eos_params[3], 'cubic_bohr', 'cubic_angstrom')
    bulk_modulus = convert_units(eos_params[1], 'rydberg_per_cubic_bohr', 'GPa')
    vols_A3 = convert_units(data[0], 'cubic_bohr', 'cubic_angstrom')
    fit_vols = np.linspace(data[0].min(), data[0].max(), 50)
    fit_vols_A3 = convert_units(fit_vols, 'cubic_bohr', 'cubic_angstrom')
    energies_eV = convert_units(data[1], 'rydberg', 'eV')
    eos_curve_eV = convert_units(eos_curve, 'rydberg', 'eV')
    fig, ax = plt.subplots()
    ax.plot(fit_vols_A3, eos_curve_eV, 'k-', label='Fit')
    ax.scatter(vols_A3, energies_eV, color='blue', label='DFT Data')
    ax.axvline(eq_vol, linestyle='--', color='black')
    ax.set_xlim(vols_A3.min() * 0.9, vols_A3.max() * 1.1)
    ax.set_ylim(energies_eV.min() - 0.1, energies_eV.max() + 0.1)
    ax.set_xlabel(r'$V$ [Å$^3$/atom]')
    ax.set_ylabel(r'$E$ [eV/atom]')
    ax.set_title(f"Birch-Murnaghan EOS for {chem} in DFT {approx}")

    label_text = (
        f"{chem}\n"
        f"{symmetry}\n"
        f"{approx}\n"
        f"K₀ = {bulk_modulus:.1f} GPa\n"
        f"V₀ = {eq_vol:.2f} Å³/atom\n"
        f"Energy Range: {stats[4]:.2f} – {stats[5]:.2f} eV"
    )

    # Add invisible dummy line to hold the label in the legend
    ax.plot([], [], ' ', label=label_text)
    ax.legend(loc='upper right', frameon=True)
    eos_filename = f"bazzett.{chem}.{symmetry}.{approx}.Birch-MurnaghanEOS.png"
    plt.savefig(eos_filename) if not display_graph else plt.show()
    plt.close()

    matrix = generate_matrix(-10, 10, 100, 'harmonic', 2)
    eigvals, eigvecs = calculate_lowest_eigenvectors(matrix, 3)
    x = np.linspace(-10, 10, 100)

    for i, (val, vec) in enumerate(zip(eigvals, eigvecs)):
        vec = vec if np.max(vec) > abs(np.min(vec)) else -vec
        fig, ax = plt.subplots()
        ax.plot(x, vec, label=fr"$\psi_{i}$, $E_{i}$ = {val:.3f} a.u.")
        ax.axhline(0, color='black')
        ax.set_ylim(-2 * np.max(np.abs(vec)), 2 * np.max(np.abs(vec)))
        ax.set_xlabel(r"$x$ [a.u.]")
        ax.set_ylabel(r"$\psi_n(x)$ [a.u.]")
        ax.set_title("Wavefunctions for a Harmonic Potential")
        ax.legend()
        annotate(ax, {})  # just adds signature
        plt.savefig(f"bazzett.harmonic.Eigenvector{i}.png") if not display_graph else plt.show()
        plt.close()
if __name__ == "__main__":
    analyze("Sn.Fd-3m.GGA-PBE.volumes_energies.dat", display_graph=True)