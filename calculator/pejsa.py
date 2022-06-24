import math


class Pejsa(object):
    _F = None
    _TE = None
    _FC = None
    _DZ = None
    Adjusted_BC = None

    def __init__(self, BC, Bullet_wt,
                 Muzzle_speed,
                 Retard_Coeff_rate,
                 Temp=0, Altitude=4600, Pressure=760,
                 Zero_range=100, Start_range=0, Special_range=585,
                 Break_Velocity=1300,
                 Standard_pressure=1000, Mayewski_constant=246,
                 Scope_ht=1.75, Impact_ht=.0, MOA=1.05,
                 Wind_speed=5, Wind_dir=3.):
        """ params:
            Muzzle_speed: Muzzle speed (fps)
            Bullet_wt: (gn)
            BC: BC
            Special_range: (yd)
            Start_range: (yd)
            Impact_ht.: (in)
            Zero_range: (yd)
            Wind_speed: (mph)
            Wind_dir.: (o'clock)
            Temp.: (Celcius)
            Altitude: (feet)
            Pressure: (mbar)
            Scope_ht.: (in)
            MOA: in./MOA at 100 yds
            Retard_Coeff_rate:
            Break_Velocity: (fps)
        """
        self._C = BC
        self._TC = Temp
        self._AL = Altitude
        self._PR = Pressure
        self._PR0 = Standard_pressure
        self._MAYEWSKI_CONST = Mayewski_constant
        self._V0 = Muzzle_speed
        self._Z = Zero_range
        self._N1 = Retard_Coeff_rate
        self._WT = Bullet_wt
        self._start_range = Start_range
        self._special_range = Special_range
        self._V1 = Break_Velocity
        self._S = Scope_ht
        self._HZ = Impact_ht
        self._MOA_VALUE = MOA
        self._VW = Wind_speed
        self._WDir = Wind_dir

        self.update_outputs()

    def update_outputs(self):
        self._F = self.retardation_coeff
        self._TE = self.temp_faht
        self.Adjusted_BC = self.adjusted_bc
        self._FC = self.adj_retard_coeff
        self._DZ = self.drop_at_zero

    @property
    def retardation_coeff(self):
        return self._C * self._MAYEWSKI_CONST * self._V0 ** 0.45

    @property
    def temp_faht(self):
        return (self._TC * 9 / 5) + 32

    @property
    def adjusted_bc(self):
        return self._C * (460 + self._TE) / (519 - self._AL / 280) * math.exp(self._AL / 31654) * (
                2 - self._PR / self._PR0)

    @property
    def adj_retard_coeff(self):
        return self._F * (460 + self._TE) / (519 - self._AL / 280) * math.exp(self._AL / 31654) * (
                2 - self._PR / self._PR0)

    @property
    def drop_at_zero(self):
        return ((41.68 / self._V0) / (
                (1 / (0 + self._Z)) - (1 / (self._FC - (0.75 + 0.00006 * self._Z) * self._N1 * self._Z)))) ** 2

    def speed_at_distance(self, distance):
        return self._V0 * (1 - 3 * self._N1 * distance / self._FC) ** (1 / self._N1)

    def speed_at_zero(self):
        return self.speed_at_distance(self._start_range)

    def speed_special_range(self):
        return self.speed_at_distance(self._special_range)

    def energy_at_speed(self, speed):
        return self._WT * speed ** 2 / 450380

    def drop_at_distance(self, energy, distance):
        if energy:
            return ((41.68 / self._V0) / ((1 / (0 + distance)) - (
                    1 / (self._FC - (0.75 + 0.00006 * distance) * self._N1 * distance)))) ** 2

    # Drop at zero clearly
    # @property
    # def drop_at_zero(self):
    #     return self.drop_at_distance(self.energy_at_speed(0), self._Z)

    def path_at_distance(self, energy, drop, distance):
        if energy:
            return -(drop + self._S) + (self._DZ + self._S + self._HZ) * distance / self._Z

    def elevn_at_distance(self, energy, path, distance):
        if energy:
            return -path / distance / self._MOA_VALUE * 100

    def windage_at_distance(self, energy, distance):
        if energy:
            return (79.2 * distance * self._VW / self._V0 / (
                    self._FC / distance - 1 - self._N1)) / distance / self._MOA_VALUE * 100 * math.sin(
                self._WDir / 12 * 2 * math.pi)

    def time_at_speed(self, energy, speed):
        if energy:
            return (self._FC / self._V0) / (1 - self._N1) * ((self._V0 / speed) ** (1 - self._N1) - 1)


if __name__ == '__main__':
    # Bullet_description = '6BR 105Lap'
    # pejsa = Pejsa(
    #     **dict(
    #         Muzzle_speed=2900,
    #         Bullet_wt=105,
    #         BC=0.530,
    #         Special_range=585,
    #         Start_range=0,
    #         Impact_ht=0.0,
    #         Zero_range=100,
    #         Wind_speed=5,
    #         Wind_dir=3.0,
    #         Temp=0,
    #         Altitude=4600,
    #         Pressure=1000,
    #         Scope_ht=1.75,
    #         MOA=1.05,
    #         Retard_Coeff_rate=0.5,
    #         Break_Velocity=1300,
    #     )
    # )

    # pejsa = Pejsa(
    #     **dict(
    #         Muzzle_speed=2624,
    #         # Muzzle_speed=2500,
    #         Bullet_wt=178,
    #         BC=0.547,
    #         # Special_range=585,
    #         # Start_range=0,
    #         Impact_ht=0.0,
    #         Zero_range=100 * 1.09361,
    #         Wind_speed=0,
    #         Wind_dir=0,
    #         Temp=15,
    #         # Altitude=1000,
    #         Pressure=760 / 1.333,
    #         Scope_ht=3.54,
    #         MOA=1.05,
    #         Retard_Coeff_rate=0.5,
    #         Break_Velocity=1300,
    #     )
    # )
    #
    # distances = [100, 200, 300, 400, 500, 1000]
    #
    # for d in distances:
    #     distance = d * 1.09361
    #     speed = pejsa.speed_at_distance(distance)
    #     energy = pejsa.energy_at_speed(speed)
    #     drop = pejsa.drop_at_distance(energy, distance)
    #     path = pejsa.path_at_distance(energy, drop, distance)
    #
    #     # print(speed, energy, drop, path)
    #     print(speed, drop)
    pass