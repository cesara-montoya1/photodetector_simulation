from scipy.constants import (
    Boltzmann as KB_J_raw,        # Constante de Boltzmann en J/K
    e as Q_E_raw,                 # Carga elemental en Coulombs
    h as H_PLANCK_J_S_raw,        # Constante de Planck en J*s
    hbar as H_BAR_J_S_raw,        # Constante de Planck reducida en J*s
    m_e as M_0_KG_raw,            # Masa en reposo del electrón en kg
    epsilon_0 as EPSILON_0_F_M_raw # Permitividad del vacío en F/m
)
from pint import UnitRegistry

# Crear el registro de unidades.
# Esto es lo que usarás para asignar y convertir unidades en todo tu código.
u = UnitRegistry()

# Definir unidades base y constantes con unidades
# Puedes usar las unidades predefinidas por pint (ej. u.joule, u.kelvin)
KB_J = KB_J_raw * u.J / u.K
Q_E = Q_E_raw * u.C
H_PLANCK_J_S = H_PLANCK_J_S_raw * u.J * u.s
H_BAR_J_S = H_BAR_J_S_raw * u.J * u.s
M_0_KG = M_0_KG_raw * u.kg
EPSILON_0_F_M = EPSILON_0_F_M_raw * u.F / u.m
