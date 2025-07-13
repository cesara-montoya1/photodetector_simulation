from constants import u

# --- Datos para el Silicio (Si) ---
SILICON_DATA = {
    "name": "Silicon",
    "electron_effective_mass": 1.08 * u.m_e,
    "hole_effective_mass": 0.55 * u.m_e,
    "band_gap_0K": 1.17 * u.eV,
    # "band_gap_300K": 1.12 * u.eV,
    # Tomado de https://www.researchgate.net/figure/The-Varshni-Parameters-of-Semiconductors_tbl1_332671531
    "varshni_alpha": 4.73e-4 * u.eV / u.K,
    "varshni_beta": 636 * u.K,
    # "electron_diffusion_coefficient_300K": 35 * u.cm**2 / u.second,
    # "hole_diffusion_coefficient_300K": 12 * u.cm**2 / u.second,
    "relative_permittivity": 11.7,
    "static_dielectric_constant": 12.0,
    "high_freq_dielectric_constant": None,
    "LO_phonon_energy": 64.35 * u.meV,
    "density": 2.332 * (10**3) * u.kg / u.m**3,
    "elastic_constant": 16.58 * (10**10) * u.N / u.m**2,
    "sound_velocity": 8.432 * (10**3) * u.meter / u.second,
    "deformation_potential": 9.0 * u.eV,
    "num_equivalent_valleys": 6,  # Para el Silicio (valle X)
    "is_polar": False,  # El Silicio es un semiconductor no polar
    # Tomado de https://www.pveducation.org/pvcdrom/materials/optical-properties-of-silicon
    "absorption_coefficient_data": {
        300: 1.73e6 * u.cm**-1,
        400: 9.52e4 * u.cm**-1,
        500: 1.11e4 * u.cm**-1,
        600: 4.14e3 * u.cm**-1,
        700: 1.9e3 * u.cm**-1,
        800: 8.5e2 * u.cm**-1,
        900: 3.06e2 * u.cm**-1,
        1000: 6.4e1 * u.cm**-1,
        1100: 3.5 * u.cm**-1,
        1200: 2.2e-2 * u.cm**-1,
    },
    "electron_lifetime": 100 * u.us,
    "hole_lifetime": 100 * u.us,
}

# --- Datos para el Germanio (Ge) ---
GERMANIUM_DATA = {
    "name": "Germanium",
    "electron_effective_mass": 0.55 * u.m_e,
    "hole_effective_mass": 0.39 * u.m_e,
    "band_gap_0K": 0.744 * u.eV,
    # "band_gap_300K": 0.66 * u.eV,
    # Tomado de https://www.researchgate.net/figure/The-Varshni-Parameters-of-Semiconductors_tbl1_332671531
    "varshni_alpha": 4.77e-4 * u.eV / u.K,
    "varshni_beta": 235 * u.K,
    # "electron_diffusion_coefficient_300K": 101 * u.cm**2 / u.second,
    # "hole_diffusion_coefficient_300K": 49 * u.cm**2 / u.second,
    "relative_permittivity": 16.2,
    "static_dielectric_constant": 16.0,
    "high_freq_dielectric_constant": None,
    "LO_phonon_energy": 37.30 * u.meV,
    "density": 5.323 * (10**3) * u.kg / u.m**3,
    "elastic_constant": 12.853 * (10**10) * u.N / u.m**2,
    "sound_velocity": 4.914 * (10**3) * u.meter / u.second,
    "deformation_potential": 11.5 * u.eV,
    "num_equivalent_valleys": 4,  # Para el Germanio (valle L)
    "is_polar": False,
    # Aproximado de https://www.ioffe.ru/SVA/NSM/Semicond/Ge/optic.html
    "absorption_coefficient_data": {
        300: 9.0e5 * u.cm**-1,
        400: 2.0e5 * u.cm**-1,
        500: 6.8e4 * u.cm**-1,
        600: 3.8e4 * u.cm**-1,
        700: 1.9e4 * u.cm**-1,
        800: 1.5e3 * u.cm**-1,
        900: 0.08e6 * u.cm**-1,
        1000: 0.07e6 * u.cm**-1,
        1100: 0.05e6 * u.cm**-1,
        1200: 0.03e6 * u.cm**-1,
    },
    "electron_lifetime": 500 * u.us,
    "hole_lifetime": 500 * u.us,
}

# --- Datos para el Arseniuro de Galio (GaAs) ---
GALLIUM_ARSENIDE_DATA = {
    "name": "Gallium Arsenide",
    "electron_effective_mass": 0.070 * u.m_e,
    "hole_effective_mass": 0.43 * u.m_e,
    "band_gap_0K": 1.519 * u.eV,
    # "band_gap_300K": 1.42 * u.eV,
    # Tomado de https://www.researchgate.net/figure/The-Varshni-Parameters-of-Semiconductors_tbl1_332671531
    "varshni_alpha": 5.41e-4 * u.eV / u.K,
    "varshni_beta": 204 * u.K,
    # "electron_diffusion_coefficient_300K": 220 * u.cm**2 / u.second,
    # "hole_diffusion_coefficient_300K": 10 * u.cm**2 / u.second,
    "relative_permittivity": 11.7,
    "static_dielectric_constant": 12.9,
    "high_freq_dielectric_constant": 10.92,
    "LO_phonon_energy": 35.36 * u.meV,
    "density": 5.36 * (10**3) * u.kg / u.m**3,
    "elastic_constant": 11.76 * (10**10) * u.N / u.m**2,
    "sound_velocity": 4.684 * (10**3) * u.meter / u.second,
    "deformation_potential": 14.0 * u.eV,
    "num_equivalent_valleys": 1,  # Para el GaAs (valle Gamma)
    "is_polar": True,  # El GaAs es un semiconductor polar
    # Aproximado de https://www.ioffe.ru/SVA/NSM/Semicond/GaAs/optic.html
    "absorption_coefficient_data": {
        300: 1.2e6 * u.cm**-1,
        400: 0.7e6 * u.cm**-1,
        500: 0.5e6 * u.cm**-1,
        600: 0.37e6 * u.cm**-1,
        700: 0.12e6 * u.cm**-1,
        800: 0.08e6 * u.cm**-1,
        900: 0.01e1 * u.cm**-1,
        1000: 1.00 * u.cm**-1,  # Fuera de la gráfica
        1100: 1e-1 * u.cm**-1,  # Fuera de la gráfica
        1200: 1e-2 * u.cm**-1,  # Fuera de la gráfica
    },
    "electron_lifetime": 5 * u.ns,
    "hole_lifetime": 10 * u.ns,
}

SEMICONDUCTOR_MATERIALS = {
    "Si": SILICON_DATA,
    "Ge": GERMANIUM_DATA,
    "GaAs": GALLIUM_ARSENIDE_DATA,
}
