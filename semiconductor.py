import numpy as np
from pint import Quantity
from constants import KB, H_PLANCK, H_BAR, Q_E, EPSILON_0
from materials_data import SEMICONDUCTOR_MATERIALS
from constants import u


class Semiconductor:
    def __init__(
        self,
        material: str,
        T: Quantity = 0 * u.K,
        N_D: Quantity = 0 * u.meter**-3,
        N_A: Quantity = 0 * u.meter**-3,
    ):
        if material not in SEMICONDUCTOR_MATERIALS:
            raise ValueError(f"Material '{material}' no soportado")

        self.data = SEMICONDUCTOR_MATERIALS[material]
        self.T = T.to("kelvin")
        self.N_D = N_D.to("meter**-3")
        self.N_A = N_A.to("meter**-3")

        # Extraer constantes necesarias
        self.m_n = self.data["electron_effective_mass"]
        self.m_p = self.data["hole_effective_mass"]
        self.Eg_0K = self.data["band_gap_0K"]
        self.alpha = self.data["varshni_alpha"]
        self.beta = self.data["varshni_beta"]
        self.is_polar = self.data["is_polar"]
        self.relative_permittivity = self.data["relative_permittivity"]
        self.elastic_constant = self.data["elastic_constant"]
        self.deformation_potential = self.data["deformation_potential"]
        self.density = self.data["density"]
        self.sound_velocity = self.data["sound_velocity"]
        self.static_dielectric_constant = self.data["static_dielectric_constant"]
        self.high_freq_dielectric_constant = self.data["high_freq_dielectric_constant"]
        self.LO_phonon_energy = self.data["LO_phonon_energy"]
        self.absorption_coefficient = self.data["absorption_coefficient"]

    @u.wraps(u.eV, None)
    def band_gap(self) -> Quantity:
        """
        Calcula la brecha de banda a la temperatura actual usando la ecuación de Varshni
        """
        T = self.T
        Eg = self.Eg_0K - (self.alpha * T**2) / (T + self.beta)
        return Eg

    @u.wraps((u.m**-3, u.m**-3), (None))
    def effective_density_of_states(self) -> tuple[Quantity, Quantity]:
        T = self.T.to("kelvin")
        Nc = 2 * ((2 * np.pi * self.m_n * KB * T) / H_PLANCK**2) ** (3 / 2)
        Nv = 2 * ((2 * np.pi * self.m_p * KB * T) / H_PLANCK**2) ** (3 / 2)
        return Nc, Nv

    @u.wraps(u.m**-3, None)
    def intrinsic_concentration(self) -> Quantity:
        Eg = self.band_gap()
        T = self.T.to("kelvin")
        Nc, Nv = self.effective_density_of_states()
        ni = np.sqrt(Nc * Nv) * np.exp(-Eg / (2 * KB * T))
        return ni

    @u.wraps((u.m**-3, u.m**-3), (None))
    def carrier_concentrations(self) -> tuple[Quantity, Quantity]:
        ni = self.intrinsic_concentration()
        N_D, N_A = self.N_D, self.N_A

        if N_D > N_A:
            n = (N_D - N_A) / 2 + np.sqrt((N_D - N_A) ** 2 / 4 + ni**2)
            p = ni**2 / n
        else:
            p = (N_A - N_D) / 2 + np.sqrt((N_A - N_D) ** 2 / 4 + ni**2)
            n = ni**2 / p

        return n, p

    @u.wraps(u.eV, None)
    def fermi_level(self) -> Quantity:
        Eg = self.band_gap()
        T = self.T
        n, p = self.carrier_concentrations()
        m_n, m_p = self.m_n, self.m_p

        term1 = Eg / 2
        term2 = (3 / 4) * KB * T * np.log((m_p / m_n))
        term3 = (KB * T / 2) * np.log((n / p))

        Ef = term1 + term2 + term3
        return Ef

    # Desde acá empieza el cálculo de las movilidades
    @u.wraps(u.cm**2 / (u.V * u.s), (None, u.kg))
    def impurities_mobility(self, eff_mass: Quantity) -> Quantity:
        T = self.T
        epsilon_r = self.relative_permittivity
        epsilon = epsilon_r * EPSILON_0
        N_i = self.N_D + self.N_A

        if N_i == 0:
            raise ValueError("There is no doping")

        # Por alguna razón recibía adimensional el valor
        m_star = eff_mass * u.kg if type(eff_mass) is float else eff_mass

        # Argumento del logaritmo (debe ser adimensional)
        log_arg = (12 * np.pi * epsilon * KB * T / (Q_E**2 * N_i ** (1 / 3))) ** 2

        num = 64 * np.sqrt(np.pi) * epsilon**2 * (2 * KB * T) ** (3 / 2)
        den = N_i * Q_E**3 * np.sqrt(m_star) * np.log(1 + log_arg)

        mu_imp = num / den

        return mu_imp

    @u.wraps(u.cm**2 / (u.V * u.s), (None, u.kg))
    def acoustic_phonons_intervalley_mobility(self, eff_mass: Quantity) -> Quantity:
        if self.is_polar:
            raise ValueError(
                "Can't calculate intervalley mobility for polar semiconductors"
            )

        # Por alguna razón recibía adimensional el valor
        m_star = eff_mass * u.kg if type(eff_mass) is float else eff_mass
        T = self.T
        Cu = self.elastic_constant
        Theta = self.deformation_potential

        num = np.sqrt(8 * np.pi) * Q_E * H_BAR**4 * Cu
        den = 3 * m_star ** (5 / 2) * (KB * T) ** (3 / 2) * Theta**2

        mu_intervalley = num / den

        return mu_intervalley

    @u.wraps(u.cm**2 / (u.V * u.s), (None, u.kg))
    def acoustic_phonons_intravalley_mobility(self, eff_mass: Quantity) -> Quantity:
        if self.is_polar:
            raise ValueError(
                "Can't calculate intravalley mobility for polar semiconductors"
            )

        # Por alguna razón recibía adimensional el valor
        m_star = eff_mass * u.kg if type(eff_mass) is float else eff_mass
        T = self.T
        rho = self.density
        v_s = self.sound_velocity
        Theta = self.deformation_potential

        num = 2 ** (3 / 2) * np.sqrt(np.pi) * Q_E * H_BAR**4 * rho * v_s**2
        den = 3 * m_star ** (5 / 2) * (KB * T) ** (3 / 2) * Theta**2

        mu_intravalley = num / den

        return mu_intravalley

    @u.wraps(u.cm**2 / (u.V * u.s), (None, u.kg))
    def optical_phonons_polar_mobility(self, eff_mass: Quantity) -> Quantity:
        if not self.is_polar:
            raise ValueError(
                "Can't calculate polar optical phonons for non-polar semiconductors"
            )

        # Por alguna razón recibía adimensional el valor
        m_star = eff_mass * u.kg if type(eff_mass) is float else eff_mass
        T = self.T
        k_0 = self.static_dielectric_constant
        k_infty = self.high_freq_dielectric_constant

        hbar_w_LO = self.LO_phonon_energy

        E_0 = (
            m_star
            * Q_E
            * hbar_w_LO
            * (1 / k_infty - 1 / k_0)
            / (4 * np.pi * H_BAR**2 * EPSILON_0)
        )

        x0 = hbar_w_LO / (KB * T)

        num = 8 * np.sqrt(2 * KB * T) * (np.exp(x0) - 1)
        den = 3 * np.sqrt(np.pi * m_star) * E_0 * (np.exp(x0) + 1)

        mu_pop = num / den

        return mu_pop

    # Las movilidades por fonones ópticos NO polares no se consideran debido a la complejidad
    # del cálculo, además la movilidad por dislocaciones tampoco se considera
    @u.wraps((u.cm**2 / (u.V * u.s), u.cm**2 / (u.V * u.s)), (None))
    def matthiesen_rule(self) -> Quantity:
        mus = []
        for m_star in [self.m_n, self.m_p]:
            inverse_terms = []
            N_i = (self.N_A + self.N_D).magnitude
            if N_i != 0:
                mu_imp = self.impurities_mobility(m_star)
                inverse_terms.append(1/mu_imp)
            if self.is_polar:
                mu_pop = self.optical_phonons_polar_mobility(m_star)
                inverse_terms.append(1/mu_pop)
            else:
                mu_intervalley = self.acoustic_phonons_intervalley_mobility(m_star)
                mu_intravalley = self.acoustic_phonons_intravalley_mobility(m_star)
                inverse_terms.append(1/mu_intervalley)
                inverse_terms.append(1/mu_intravalley)
            print(inverse_terms)
            mu_total = 1 / sum(inverse_terms)
            mus.append(mu_total)

        mu_n, mu_p = mus

        return mu_n, mu_p
