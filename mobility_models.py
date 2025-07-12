import numpy as np
from constants import KB_J, Q_E, H_BAR_J_S, M_0_KG, EPSILON_0_F_M, u

# --- Funciones de Movilidad ---


# El decorador @u.wraps especifica las unidades de entrada y salida.
# Las entradas con "None" indican que el parámetro es adimensional o un factor.
# El resultado se convierte automáticamente a las unidades especificadas.
@u.wraps(
    u.cm**2 / (u.volt * u.second),  # Unidades de salida
    [
        u.kelvin,
        u.meter**-3,
        None,
        None,
    ],  # Unidades de entrada: Temp, Conc, m_eff, rel_perm
)
def calculate_impurity_mobility(
    temperature,
    total_impurity_concentration,
    effective_mass: float,
    relative_permittivity: float,
):
    """
    Calcula la movilidad por dispersión de impurezas ionizadas.
    Retorna movilidad en cm^2/(V*s).
    """
    if total_impurity_concentration.magnitude <= 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    m_star_kg = effective_mass * M_0_KG
    epsilon_Fm = relative_permittivity * EPSILON_0_F_M

    # Primer término (Factor A)
    term_A_numerator = (
        64 * np.sqrt(np.pi) * (epsilon_Fm**2) * (2 * KB_J * temperature) ** (1.5)
    )
    term_A_denominator = total_impurity_concentration * (Q_E**3) * np.sqrt(m_star_kg)

    if term_A_denominator.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)
    term_A = term_A_numerator / term_A_denominator

    # Segundo término (dentro del logaritmo)
    term_B_inside_log_numerator = 12 * np.pi * epsilon_Fm * KB_J * temperature
    term_B_inside_log_denominator = (Q_E**2) * (total_impurity_concentration ** (1 / 3))

    if term_B_inside_log_denominator.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    term_B_inside_log = (
        term_B_inside_log_numerator / term_B_inside_log_denominator
    ).to_base_units() ** 2

    log_term = np.log(1 + term_B_inside_log.magnitude)
    if log_term == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    mu_i_m2_per_Vs = term_A / log_term

    return mu_i_m2_per_Vs


@u.wraps(
    u.cm**2 / (u.volt * u.second),  # Unidades de salida
    [
        u.kelvin,
        None,
        u.meter / u.second,
        u.joule,
        u.kilogram / u.meter**3,
    ],  # Unidades de entrada
)
def calculate_intravalley_mobility(
    temperature, effective_mass: float, sound_velocity, deformation_potential, density
):
    """
    Calcula la movilidad por fonones acústicos (intravalley).
    Retorna movilidad en cm^2/(V*s).
    """
    m_star_kg = effective_mass * M_0_KG

    numerator = (
        2 ** (1.5)
        * np.sqrt(np.pi)
        * Q_E
        * (H_BAR_J_S**4)
        * density
        * (sound_velocity**2)
    )
    denominator = (
        3
        * (m_star_kg ** (2.5))
        * (KB_J * temperature) ** (1.5)
        * (deformation_potential**2)
    )

    if denominator.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    mu_m2_per_Vs = numerator / denominator
    return mu_m2_per_Vs


@u.wraps(
    u.cm**2 / (u.volt * u.second),  # Unidades de salida
    [u.kelvin, None, u.pascal, u.joule],  # Unidades de entrada
)
def calculate_intervalley_mobility(
    temperature, effective_mass: float, elastic_constant, deformation_potential
):
    """
    Calcula la movilidad por fonones acústicos (intervalley).
    Retorna movilidad en cm^2/(V*s).
    """
    m_star_kg = effective_mass * M_0_KG

    numerator = np.sqrt(8 * np.pi) * Q_E * (H_BAR_J_S**4) * elastic_constant
    denominator = (
        3
        * (m_star_kg ** (2.5))
        * (KB_J * temperature) ** (1.5)
        * (deformation_potential**2)
    )

    if denominator.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    mu_m2_per_Vs = numerator / denominator
    return mu_m2_per_Vs


@u.wraps(
    u.cm**2 / (u.volt * u.second),  # Unidades de salida
    [u.kelvin, None, u.joule, None, None],  # Unidades de entrada
)
def calculate_polar_optical_mobility(
    temperature,
    effective_mass: float,
    LO_phonon_energy,
    relative_permittivity: float,
    high_freq_permittivity: float,
):
    """
    Calcula la movilidad por fonones ópticos polares (mu_pop).
    Retorna movilidad en cm^2/(V*s).
    """
    m_star_kg = effective_mass * M_0_KG

    # x0 debe ser adimensional
    x0 = (LO_phonon_energy / (KB_J * temperature)).to_base_units().magnitude

    E0_val_numerator = m_star_kg * Q_E * LO_phonon_energy
    E0_val_denominator = 4 * np.pi * (H_BAR_J_S**2) * EPSILON_0_F_M

    if E0_val_denominator.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    E0_val = (E0_val_numerator / E0_val_denominator) * (
        1 / high_freq_permittivity - 1 / relative_permittivity
    )

    numerator_mu = 8 * np.sqrt(2 * KB_J * temperature) * (np.exp(x0) - 1)
    denominator_mu = 3 * np.sqrt(np.pi * m_star_kg) * E0_val * (np.exp(x0) + 1)

    if denominator_mu.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    mu_m2_per_Vs = numerator_mu / denominator_mu
    return mu_m2_per_Vs


@u.wraps(
    u.cm**2 / (u.volt * u.second),  # Unidades de salida
    [
        u.kelvin,
        None,
        u.meter / u.second,
        u.joule,
        u.kilogram / u.meter**3,
        u.joule,
    ],  # Unidades de entrada
)
def calculate_nonpolar_optical_mobility(
    temperature,
    effective_mass: float,
    sound_velocity,
    deformation_potential,
    density,
    LO_phonon_energy,
):
    """
    Calcula la movilidad por fonones ópticos no polares (mu_op).
    La implementación de la integral f(x) es compleja y requiere integración numérica.
    Esto es un PLACEHOLDER.
    Retorna movilidad en cm^2/(V*s).
    """
    print(
        "Advertencia: El modelo de movilidad por fonones ópticos no polares (f(x)) es un PLACEHOLDER y necesita implementación numérica o un modelo simplificado."
    )

    # Las entradas ya vienen en las unidades especificadas por @u.wraps
    # Cálculos dummy por ser un placeholder

    return (
        np.inf * u.cm**2 / (u.volt * u.second)
    )  # Retorna inf con unidades, como ejemplo


@u.wraps(
    u.cm**2 / (u.volt * u.second),  # Unidades de salida
    [
        u.kelvin,
        u.meter**-3,
        None,
        None,
        u.meter**-2,
        u.meter,
        None,
    ],  # Unidades de entrada
)
def calculate_dislocation_mobility(
    temperature,
    carrier_concentration,
    effective_mass: float,
    relative_permittivity: float,
    dislocation_density,
    dislocation_distance,
    filling_factor: float,
):
    """
    Calcula la movilidad por dispersión de dislocaciones.
    Retorna movilidad en cm^2/(V*s).
    """
    if dislocation_density.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    m_star_kg = effective_mass * M_0_KG
    epsilon_Fm = relative_permittivity * EPSILON_0_F_M

    # Longitud de Debye (lambda_D)
    lambda_D_numerator = epsilon_Fm * KB_J * temperature
    lambda_D_denominator = (Q_E**2) * carrier_concentration

    if lambda_D_denominator.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    lambda_D_m = np.sqrt((lambda_D_numerator / lambda_D_denominator).to(u.meter**2))

    # Movilidad por dislocaciones
    numerator = (
        30
        * np.sqrt(2)
        * (epsilon_Fm**2)
        * (dislocation_distance**2)
        * (KB_J * temperature) ** (1.5)
    )
    denominator = (
        dislocation_density
        * (Q_E**3)
        * (filling_factor**2)
        * lambda_D_m
        * np.sqrt(m_star_kg)
    )

    if denominator.magnitude == 0:
        return np.inf * u.cm**2 / (u.volt * u.second)

    mu_dis_m2_per_Vs = numerator / denominator
    return mu_dis_m2_per_Vs
