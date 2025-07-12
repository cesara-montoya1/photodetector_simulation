from constants import u

# --- Datos para el Silicio (Si) ---
SILICON_DATA = {
    "name": "Silicon",
    "electron_effective_mass": 1.08 * u.m_e,
    "hole_effective_mass": 0.55 * u.m_e,
    "band_gap_300K": 1.12 * u.eV,
    "electron_diffusion_coefficient_300K": 35 * u.cm**2 / u.second,
    "hole_diffusion_coefficient_300K": 12 * u.cm**2 / u.second,
    "relative_permittivity": 12.0,
    "high_freq_permittivity": None,
    "LO_phonon_energy": 64.35 * u.meV,
    "density": 2.332 * (10**3) * u.kg / u.m**3,
    "elastic_constant": 16.58 * (10**10) * u.N / u.m**2,
    "sound_velocity": 8.432 * (10**3) * u.meter / u.second,
    "deformation_potential": 9.0 * u.eV,
    # "num_equivalent_valleys": 6,             # Para el Silicio (valle X)
    "is_polar": False,                       # El Silicio es un semiconductor no polar
    # "absorption_coefficient_data": {         # Ejemplo de datos de absorción (longitud de onda en nm: alpha en cm^-1)
    #   200: 1.0e5, 300: 1.0e4, 400: 1.0e3, 500: 1.0e2, 600: 1.0e1, 700: 1.0e0, 800: 1.0e-1, 900: 1.0e-2, 1000: 1.0e-3, 1100: 1.0e-4
    # },
    # "electron_lifetime": 1.0e-6 * u.second,  # Ejemplo: 1 microsegundo
    # "hole_lifetime": 1.0e-6 * u.second       # Ejemplo: 1 microsegundo
}

# --- Datos para el Germanio (Ge) ---
GERMANIUM_DATA = {
    "name": "Germanium",
    "electron_effective_mass": 0.55 * u.m_e,
    "hole_effective_mass": 0.39 * u.m_e,
    "band_gap_300K": 0.66 * u.eV,
    "electron_diffusion_coefficient_300K": 101 * u.cm**2 / u.second,
    "hole_diffusion_coefficient_300K": 49 * u.cm**2 / u.second,
    "relative_permittivity": 16.0,
    "high_freq_permittivity": None,
    "LO_phonon_energy": 37.30 * u.meV,
    "density": 5.323 * (10**3) * u.kg / u.m**3,
    "elastic_constant": 12.853 * (10**10) * u.N / u.m**2,
    "sound_velocity": 4.914 * (10**3) * u.meter / u.second,
    "deformation_potential": 11.5 * u.eV,
    # "num_equivalent_valleys": 4,             # Para el Germanio (valle L)
    "is_polar": False,
    # "dislocation_density": 0.0 * u.cm**-2,
    # "dislocation_distance": 0.0 * u.cm,
    # "filling_factor": 0.0,
    # "absorption_coefficient_data": {
    #   500: 1.0e5, 600: 1.0e4, 700: 1.0e3, 800: 1.0e2, 900: 1.0e1, 1000: 1.0e0, 1100: 1.0e-1, 1200: 1.0e-2, 1300: 1.0e-3, 1400: 1.0e-4
    # },
    # "electron_lifetime": 1.0e-6 * u.second,
    # "hole_lifetime": 1.0e-6 * u.second
}

# --- Datos para el Arseniuro de Galio (GaAs) ---
GALLIUM_ARSENIDE_DATA = {
    "name": "Gallium Arsenide",
    "electron_effective_mass": 0.070 * u.m_e,
    "hole_effective_mass": 0.43 * u.m_e,
    "band_gap_300K": 1.42 * u.eV,
    "electron_diffusion_coefficient_300K": 220 * u.cm**2 / u.second,
    "hole_diffusion_coefficient_300K": 10 * u.cm**2 / u.second,
    "relative_permittivity": 12.9,
    "high_freq_permittivity": 10.92,
    "LO_phonon_energy": 35.36 * u.meV,
    "density": 5.36 * (10**3) * u.kg / u.m**3,
    "elastic_constant": 11.76 * (10**10) * u.N / u.m**2,
    "sound_velocity": 4.684 * (10**3) * u.meter / u.second,
    "deformation_potential": 14.0 * u.eV,
    # "num_equivalent_valleys": 1,             # Para el GaAs (valle Gamma)
    "is_polar": True,                        # El GaAs es un semiconductor polar
    # "dislocation_density": 0.0 * u.cm**-2,
    # "dislocation_distance": 0.0 * u.cm,
    # "filling_factor": 0.0,
    # "absorption_coefficient_data": {
    #   400: 1.0e5, 500: 1.0e4, 600: 1.0e3, 700: 1.0e2, 800: 1.0e1, 900: 1.0e0, 1000: 1.0e-1, 1100: 1.0e-2, 1200: 1.0e-3, 1300: 1.0e-4
    # },
    # "electron_lifetime": 1.0e-8 * u.second,  # Ejemplo: 10 nanosegundos
    # "hole_lifetime": 1.0e-8 * u.second       # Ejemplo: 10 nanosegundos
}

SEMICONDUCTOR_MATERIALS = {
    "Si": SILICON_DATA,
    "Ge": GERMANIUM_DATA,
    "GaAs": GALLIUM_ARSENIDE_DATA,
}
