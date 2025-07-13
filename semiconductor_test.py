import numpy as np
import matplotlib.pyplot as plt

from semiconductor import (
    Semiconductor,
)  # Asegúrate que el nombre del archivo sea correcto
from constants import u 

# Definir rangos de temperatura
temperatures = np.linspace(100, 500, 15) * u.kelvin

# Valores de dopaje tipo N (puede probar también para tipo P si se desea)
dopings = [0, 1e15, 1e20, 1e25, 1e30]  # en 1/m³
colors = plt.cm.viridis(np.linspace(0, 1, len(dopings)))

# Preparar figura
plt.figure(figsize=(10, 6))

for doping, color in zip(dopings, colors):
    sigmas = []
    for T in temperatures:
        semi = Semiconductor("Si", T, N_D=doping * u.m**-3)
        n, p = semi.carrier_concentrations()
        mu_n, mu_p = semi.matthiesen_rule()
        sigma = (n * u.e * mu_n + p * u.e * mu_p).to("S/m")
        sigmas.append(sigma.magnitude)

    label = f"$N_D = {doping:.0e}$"
    plt.semilogy(temperatures.magnitude, sigmas, label=label, color=color, marker="o")

# Configuración del gráfico
plt.xlabel("Temperatura [K]")
plt.ylabel("Conductividad eléctrica [S/m]")
plt.title("Variación de la conductividad con temperatura y dopaje (Si)")
plt.grid(True, alpha=0.3)
plt.legend(title="Dopaje tipo N")
plt.tight_layout()
plt.show()
