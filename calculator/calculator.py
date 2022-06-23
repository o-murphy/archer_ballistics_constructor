from typing import Union, Iterable
import math


class Pejsa(object):
    _F = None
    _TE = None
    _FC = None
    _DZ = None
    Adjusted_BC = None

    def __init__(self, BC, Bullet_wt,
                 Temp, Altitude, Pressure,
                 Muzzle_speed,
                 Retard_Coeff_rate,
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
        print(self._V0, self._N1, self._FC, distance)
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


class DragFunctions(object):
    G1 = (
        (0.000, 0.263), (0.050, 0.256), (0.100, 0.249), (0.150, 0.241), (0.200, 0.234), (0.250, 0.228), (0.300, 0.221),
        (0.350, 0.216), (0.400, 0.210), (0.450, 0.206), (0.500, 0.203), (0.550, 0.202), (0.600, 0.203), (0.700, 0.217),
        (0.725, 0.223), (0.750, 0.231), (0.775, 0.242), (0.800, 0.255), (0.825, 0.271), (0.850, 0.290), (0.875, 0.314),
        (0.900, 0.342), (0.925, 0.373), (0.950, 0.408), (0.975, 0.445), (1.000, 0.480), (1.025, 0.514), (1.050, 0.543),
        (1.075, 0.568), (1.100, 0.588), (1.125, 0.605), (1.150, 0.619), (1.200, 0.639), (1.250, 0.652), (1.300, 0.659),
        (1.350, 0.662), (1.400, 0.662), (1.450, 0.661), (1.500, 0.657), (1.550, 0.653), (1.600, 0.647), (1.650, 0.641),
        (1.700, 0.635), (1.750, 0.628), (1.800, 0.621), (1.850, 0.614), (1.900, 0.607), (1.950, 0.600), (2.000, 0.593),
        (2.050, 0.587), (2.100, 0.580), (2.150, 0.574), (2.200, 0.569), (2.250, 0.563), (2.300, 0.558), (2.350, 0.553),
        (2.400, 0.548), (2.450, 0.544), (2.500, 0.540), (2.600, 0.532), (2.700, 0.526), (2.800, 0.521), (2.900, 0.517),
        (3.000, 0.513), (3.100, 0.510), (3.200, 0.508), (3.300, 0.507), (3.400, 0.505), (3.500, 0.504), (3.600, 0.503),
        (3.700, 0.502), (3.800, 0.502), (3.900, 0.501), (4.000, 0.501), (4.200, 0.500), (4.400, 0.500), (4.600, 0.499),
        (4.800, 0.499), (5.000, 0.499)
    )
    # G7 = (
    #     (0.000, 0.120), (0.050, 0.120), (0.100, 0.120), (0.150, 0.119), (0.200, 0.119), (0.250, 0.119),
    #     (0.300, 0.119),
    #     (0.350, 0.119), (0.400, 0.119), (0.450, 0.119), (0.500, 0.119), (0.550, 0.119), (0.600, 0.119),
    #     (0.650, 0.120),
    #     (0.700, 0.120), (0.725, 0.121), (0.750, 0.122), (0.775, 0.123), (0.800, 0.124), (0.825, 0.127),
    #     (0.850, 0.131),
    #     (0.875, 0.137), (0.900, 0.146), (0.925, 0.166), (0.950, 0.205), (0.975, 0.299), (1.000, 0.380),
    #     (1.025, 0.402),
    #     (1.050, 0.404), (1.075, 0.403), (1.100, 0.401), (1.125, 0.399), (1.150, 0.396), (1.200, 0.388),
    #     (1.250, 0.381),
    #     (1.300, 0.373), (1.350, 0.366), (1.400, 0.358), (1.500, 0.344), (1.550, 0.338), (1.600, 0.332),
    #     (1.650, 0.326),
    #     (1.700, 0.321), (1.750, 0.316), (1.800, 0.312), (1.850, 0.308), (1.900, 0.304), (1.950, 0.301),
    #     (2.000, 0.298),
    #     (2.050, 0.295), (2.100, 0.292), (2.150, 0.289), (2.200, 0.286), (2.250, 0.283), (2.300, 0.281),
    #     (2.350, 0.278),
    #     (2.400, 0.275), (2.450, 0.273), (2.500, 0.270), (2.550, 0.267), (2.600, 0.264), (2.650, 0.262),
    #     (2.700, 0.259),
    #     (2.750, 0.256), (2.800, 0.253), (2.850, 0.251), (2.900, 0.248), (2.950, 0.245), (3.000, 0.242),
    #     (3.100, 0.237),
    #     (3.200, 0.231), (3.300, 0.226), (3.400, 0.221), (3.500, 0.215), (3.600, 0.211), (3.700, 0.206),
    #     (3.800, 0.202),
    #     (3.900, 0.198), (4.000, 0.194), (4.200, 0.186), (4.400, 0.179), (4.600, 0.173), (4.800, 0.167),
    #     (5.000, 0.162)
    # )
    #

    G7 = (
        (0.0, 0.11980000138282776), (0.05000000074505806, 0.11969999969005585),
        (0.10000000149011612, 0.11959999799728394), (0.15000000596046448, 0.11940000206232071),
        (0.20000000298023224, 0.1193000003695488), (0.25, 0.11940000206232071),
        (0.30000001192092896, 0.11940000206232071), (0.3499999940395355, 0.11940000206232071),
        (0.4000000059604645, 0.1193000003695488), (0.44999998807907104, 0.1193000003695488),
        (0.5, 0.11940000206232071), (0.550000011920929, 0.1193000003695488),
        (0.6000000238418579, 0.11940000206232071), (0.6499999761581421, 0.11969999969005585),
        (0.699999988079071, 0.12020000070333481), (0.7250000238418579, 0.12070000171661377),
        (0.75, 0.12150000035762787), (0.7749999761581421, 0.1225999966263771), (0.800000011920929, 0.1242000013589859),
        (0.824999988079071, 0.1265999972820282), (0.8500000238418579, 0.1306000053882599), (0.875, 0.13680000603199005),
        (0.8999999761581421, 0.14640000462532043), (0.925000011920929, 0.16599999368190765),
        (0.949999988079071, 0.2054000049829483), (0.9750000238418579, 0.2992999851703644), (1.0, 0.38029998540878296),
        (1.024999976158142, 0.40149998664855957), (1.0499999523162842, 0.4043000042438507),
        (1.0750000476837158, 0.4034000039100647), (1.100000023841858, 0.40139999985694885), (1.125, 0.3986999988555908),
        (1.149999976158142, 0.3955000042915344), (1.2000000476837158, 0.38839998841285706), (1.25, 0.38100001215934753),
        (1.2999999523162842, 0.373199999332428), (1.350000023841858, 0.36570000648498535),
        (1.399999976158142, 0.3580000102519989), (1.5, 0.3440000116825104), (1.5499999523162842, 0.3375999927520752),
        (1.600000023841858, 0.33149999380111694), (1.649999976158142, 0.32600000500679016),
        (1.7000000476837158, 0.32089999318122864), (1.75, 0.3160000145435333), (1.7999999523162842, 0.3116999864578247),
        (1.850000023841858, 0.3077999949455261), (1.899999976158142, 0.3041999936103821),
        (1.9500000476837158, 0.3009999990463257), (2.0, 0.2980000078678131), (2.049999952316284, 0.29510000348091125),
        (2.0999999046325684, 0.2921999990940094), (2.1500000953674316, 0.2892000079154968),
        (2.200000047683716, 0.2863999903202057), (2.25, 0.28349998593330383), (2.299999952316284, 0.2806999981403351),
        (2.3499999046325684, 0.27790001034736633), (2.4000000953674316, 0.2752000093460083),
        (2.450000047683716, 0.27250000834465027), (2.5, 0.26969999074935913), (2.549999952316284, 0.2669999897480011),
        (2.5999999046325684, 0.26429998874664307), (2.6500000953674316, 0.2615000009536743),
        (2.700000047683716, 0.2587999999523163), (2.75, 0.25609999895095825), (2.799999952316284, 0.2533000111579895),
        (2.8499999046325684, 0.25060001015663147), (2.9000000953674316, 0.24789999425411224),
        (2.950000047683716, 0.2451000064611435), (3.0, 0.24240000545978546), (3.0999999046325684, 0.23680000007152557),
        (3.200000047683716, 0.2312999963760376), (3.299999952316284, 0.22579999268054962),
        (3.4000000953674316, 0.22050000727176666), (3.5, 0.21539999544620514),
        (3.5999999046325684, 0.21060000360012054), (3.700000047683716, 0.20600000023841858),
        (3.799999952316284, 0.20170000195503235), (3.9000000953674316, 0.19750000536441803), (4.0, 0.19349999725818634),
        (4.199999809265137, 0.18610000610351562), (4.400000095367432, 0.179299995303154),
        (4.599999904632568, 0.17299999296665192), (4.800000190734863, 0.1671999990940094), (5.0, 0.16179999709129333))


class Constant(object):
    # R = 8.31446262
    # y = 7 / 5
    # tk0 = 273.15
    # M = 0.0289645

    # def get_speed_of_sound(self):
    #     tk = self.tk0 + self.tc
    #     c = math.sqrt(self.y * self.R * tk / self.M)
    #     c_simple = 331.3 * math.sqrt(1 + self.tc / 273.15)
    #
    #     return c_simple, c

    # class SpeedOfSound(object):
    # T: float  # temperature deg C
    # PL: float  # pressure
    # Rh: float  # relative humidity
    # Xc: float = None  # Mole fraction of carbon dioxide
    # Xw: float = None  # Mole fraction of water vapour
    # H: float = None  # respectively molecular concentration of water vapour
    # C1: float = None  # Intermediate calculations
    # C2: float = None
    # C3: float = None
    # ENH: float = None
    # PSV: float = None
    # PSV1: float = None
    # PSV2: float = None
    # T_kel: float = None  # ambient temperature (Kelvin)
    # StrMsg: float = None  # alert text

    @staticmethod
    def speed_of_sound(t: float = 26, p: float = 760, rh: float = 50):
        kelvin = 273.15  # For converting to Kelvin
        e = 2.71828182845904523536
        # C: float = None  # speed
        # kpa = p * 1000

        pa = p / 7.501 * 1000  # 760mmHg ~= 101,325kpa

        if rh > 100 or rh < 0:
            raise ValueError("Data out of range: Relative humidity must be between 0 and 100%")

        t_kel = kelvin + t  # Measured ambient temp

        # Molecular concentration of water vapour calculated from Rh
        # using Giacomos method by Davis (1991) as implemented in DTU report 11b-1997
        enh = 3.141593 * 10 ** -8 * pa + 1.00062 + t ** 2 * 5.6 * 10 ** -7

        # These commented lines correspond to values used in Cramer (Appendix)
        # PSV1 = T_kel ** 2 * 1.2811805 * 10 ** -5 -1.9509874 * 10 ** -2 * T_kel
        # PSV2 = 34.04926034 - 6.3536311 * 10 ** 3 / T_kel
        psv1 = t_kel ** 2 * 1.2378847 * 10 ** -5 - 1.9121316 * 10 ** -2 * t_kel
        psv2 = 33.93711047 - 6.3431645 * 10 ** 3 / t_kel

        psv = e ** psv1 * e ** psv2
        h = rh * enh * psv / pa
        xw = h / 100.0

        # Xc = 314.0 * 10 ** -6
        xc = 400.0 * 10 ** -6

        # Speed calculated using the method
        # of Cramer from JASA vol 93 p. 2510

        c1 = 0.603055 * t + 331.5024 - t ** 2 * 5.28 * 10 ** -4 + (
                0.1495874 * t + 51.471935 - t ** 2 * 7.82 * 10 ** -4) * xw
        c2 = (-1.82 * 10 ** -7 + 3.73 * 10 ** -8 * t - t ** 2 * 2.93 * 10 ** -10) * pa + (
                -85.20931 - 0.228525 * t + t ** 2 * 5.91 * 10 ** -5) * xc
        c3 = xw ** 2 * 2.835149 - pa ** 2 * 2.15 * 10 ** -13 + xc ** 2 * 29.179762 + 4.86 * 10 ** -4 * xw * pa * xc

        c = c1 + c2 - c3
        return c


# print(Constant.speed_of_sound(26, 760, 50))


class Calculator(object):
    def __init__(self, w: float = 90, d: float = .243, bc: Union[float, list[(float, int)]] = 0.218,
                 df_type: tuple = None,
                 atmo: tuple = None):
        self._width = w
        self._diameter = d
        self._bc = bc
        self._df_type = df_type
        self._df_data = None
        self._speed_of_sound = None
        self.speed_of_sound = atmo
        self.calculate_df()

    @property
    def speed_of_sound(self):
        return self._speed_of_sound

    @speed_of_sound.setter
    def speed_of_sound(self, atmo: tuple):
        self._speed_of_sound = Constant().speed_of_sound(*atmo)
        self.calculate_df()

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value
        self.calculate_df()

    @property
    def diameter(self) -> float:
        return self._diameter

    @diameter.setter
    def diameter(self, value: float):
        self._diameter = value
        self.calculate_df()

    @property
    def bc(self) -> Union[float, list[(float, int)]]:
        return self._bc

    @bc.setter
    def bc(self, value: Union[float, list[(float, int)]]):
        self._bc = value
        self.calculate_df()

    @property
    def df_type(self) -> tuple:
        return self._df_type

    @df_type.setter
    def df_type(self, value: tuple):
        self._df_type = value
        self.calculate_df()

    @property
    def df_data(self) -> Iterable[tuple[float, int]]:
        return self._df_data

    @df_data.setter
    def df_data(self, value: Iterable[tuple[float, float]]):
        self._df_data = value
        self._df_type = None

    def calculate_df(self):
        if self._df_type:
            if isinstance(self._bc, float):
                self.calculate_drag_function()
            elif isinstance(self._bc, list):
                if len(self._bc) > 1:
                    self.calculate_drag_function_multi_bc()
                else:
                    self._bc = self._bc[0][0]

    def sectional_density(self) -> float:
        """ params:
            w: weight in pounds
            d: diameter in inches
        """
        return self._width / (self._diameter ** 2)

    def form_factor_by_bullet_data(self, bc):
        return self.sectional_density() / 7000 / bc

    @staticmethod
    def counted_drag_coefficient(form_factor, cdst):
        return cdst * form_factor

    def calculate_drag_function(self):
        form_factor = self.form_factor_by_bullet_data(self._bc, )
        drag_function = []
        for vst, cdst in self._df_type:
            cd = self.counted_drag_coefficient(form_factor, cdst)
            drag_function.append((vst, cd))
        self._df_data = drag_function

    def bc_extended(self):

        bc_mah = [[i[0], i[1] / self.speed_of_sound] for i in self._bc]
        bc_mah[0][1] = self._df_type[-1][0]
        bc_mah.insert(len(bc_mah), [bc_mah[-1][0], self._df_type[0][0]])
        bc_extended = [bc_mah[0][0], ]

        for i in range(1, len(bc_mah)):
            bc_max, v_max = bc_mah[i - 1]
            bc_min, v_min = bc_mah[i]
            df_part = list(filter(lambda point: v_max > point[0] >= v_min, self.df_type))
            ddf = len(df_part)
            bc_delta = (bc_max - bc_min) / ddf
            for j in range(ddf):
                bc_extended.append(bc_max - bc_delta * j)

        return bc_extended

    def calculate_drag_function_multi_bc(self):
        bc_extended = self.bc_extended()
        drag_function = []
        for i, (vst, cdst) in enumerate(self._df_type):
            bc = bc_extended[len(bc_extended) - 1 - i]
            form_factor = self.form_factor_by_bullet_data(bc)
            cd = self.counted_drag_coefficient(form_factor, cdst)
            drag_function.append((vst, cd))
        drag_function.sort()
        self._df_data = drag_function


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    calculator = Calculator(w=178, d=0.308, bc=[
        (0.595, 853.44),
        (0.58, 731.52),
        (0.575, 624.84),
        # (0.55, 0)
    ], df_type=DragFunctions.G1, atmo=(15, 760, 50))

    # calculator = Calculator(w=178, d=0.308, bc=0.268, df_type=DragFunctions.G7, atmo=(15, 760, 50))

    datasheet = '\n'.join([str(cd).replace('.', ',') for v, cd in calculator.df_data])

    cb = QApplication.clipboard()
    cb.clear(mode=cb.Clipboard)
    cb.setText(datasheet, mode=cb.Clipboard)

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

    pejsa = Pejsa(
        **dict(
            Muzzle_speed=2900,
            Bullet_wt=105,
            BC=0.530,
            Special_range=585,
            Start_range=0,
            Impact_ht=0.0,
            Zero_range=100,
            Wind_speed=5,
            Wind_dir=3.0,
            Temp=0,
            Altitude=4600,
            Pressure=1000,
            Scope_ht=1.75,
            MOA=1.05,
            Retard_Coeff_rate=0.5,
            Break_Velocity=1300,
        )
    )

    distance = 100

    speed = pejsa.speed_at_distance(distance)
    energy = pejsa.energy_at_speed(speed)
    drop = pejsa.drop_at_distance(energy, distance)
    path = pejsa.path_at_distance(energy, drop, distance)

    print(speed, energy, drop, path)