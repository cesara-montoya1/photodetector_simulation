from scipy.constants import (
    Boltzmann as KB_J_raw,        # Constante de Boltzmann en J/K
    h as H_PLANCK_J_S_raw,        # Constante de Planck en J*s
    hbar as H_BAR_J_S_raw,        # Constante de Planck reducida en J*s
    epsilon_0 as EPSILON_0_F_M_raw, # Permitividad del vacío en F/m
)
from pint import UnitRegistry

# Crear el registro de unidades.
# Esto es lo que usarás para asignar y convertir unidades en todo tu código.
u = UnitRegistry()

# Definir unidades base y constantes con unidades
KB = KB_J_raw * u.J / u.K
Q_E = (1 * u.e).to(u.C)
H_PLANCK = H_PLANCK_J_S_raw * u.J * u.s
H_BAR = H_BAR_J_S_raw * u.J * u.s
M_E = (1 * u.m_e).to(u.kg)
EPSILON_0 = EPSILON_0_F_M_raw * u.F / u.m
C_LIGHT = (1 * u.speed_of_light).to(u.m / u.s)
