import matplotlib.pyplot as plt

"""parse visconsity into nest dictionary with return visc of data"""
def parse_viscosity_data(filename):
    viscosity_data = {}
    with open(filename, 'r') as f:
        for line in f:
            if line.strip().startswith('#') or not line.strip():
                continue
            parts = line.strip().split()
            gas = ' '.join(parts[:-3])
            C = float(parts[-3])
            T0 = float(parts[-2])
            mu0 = float(parts[-1])
            viscosity_data[gas.lower()] = {'viscosity': C, 'reference_temperature': T0, 'reference_viscosity': mu0}
    return viscosity_data

"""calculates viscosity mu(t) for gast/temp given"""
def calculate_viscosity(T, gas, viscosity_data):
    gas_key = gas.lower()
    if gas_key not in viscosity_data:
        raise ValueError(f"Gas '{gas}' not found in viscosity data.")
    C = viscosity_data[gas_key]['viscosity']
    T0 = viscosity_data[gas_key]['reference_temperature']
    mu0 = viscosity_data[gas_key]['reference_viscosity']
    mu = mu0 * ((T0 + C) / (T + C)) * (T / T0) ** 1.5
    return mu

def plot_viscosity():
    gases = ['air', 'carbon dioxide', 'hydrogen']
    T_values = list(range(223, 374, 5))  # 223 to 373 K
    viscosity_data = parse_viscosity_data('viscosity_of_gases.dat')
    plt.figure(figsize=(8, 6))
    for gas in gases:
        mu_values = [calculate_viscosity(T, gas, viscosity_data) for T in T_values]
        plt.plot(T_values, mu_values, label=gas.capitalize())
    plt.title('Viscosity vs Temperature for Selected Gases')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Viscosity (Pa·s)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    plot_viscosity()