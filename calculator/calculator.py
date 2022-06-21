from typing import Callable, Iterator, Union, Optional, Iterable
import math


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
    #     (0.000, 0.120), (0.050, 0.120), (0.100, 0.120), (0.150, 0.119), (0.200, 0.119), (0.250, 0.119), (0.300, 0.119),
    #     (0.350, 0.119), (0.400, 0.119), (0.450, 0.119), (0.500, 0.119), (0.550, 0.119), (0.600, 0.119), (0.650, 0.120),
    #     (0.700, 0.120), (0.725, 0.121), (0.750, 0.122), (0.775, 0.123), (0.800, 0.124), (0.825, 0.127), (0.850, 0.131),
    #     (0.875, 0.137), (0.900, 0.146), (0.925, 0.166), (0.950, 0.205), (0.975, 0.299), (1.000, 0.380), (1.025, 0.402),
    #     (1.050, 0.404), (1.075, 0.403), (1.100, 0.401), (1.125, 0.399), (1.150, 0.396), (1.200, 0.388), (1.250, 0.381),
    #     (1.300, 0.373), (1.350, 0.366), (1.400, 0.358), (1.500, 0.344), (1.550, 0.338), (1.600, 0.332), (1.650, 0.326),
    #     (1.700, 0.321), (1.750, 0.316), (1.800, 0.312), (1.850, 0.308), (1.900, 0.304), (1.950, 0.301), (2.000, 0.298),
    #     (2.050, 0.295), (2.100, 0.292), (2.150, 0.289), (2.200, 0.286), (2.250, 0.283), (2.300, 0.281), (2.350, 0.278),
    #     (2.400, 0.275), (2.450, 0.273), (2.500, 0.270), (2.550, 0.267), (2.600, 0.264), (2.650, 0.262), (2.700, 0.259),
    #     (2.750, 0.256), (2.800, 0.253), (2.850, 0.251), (2.900, 0.248), (2.950, 0.245), (3.000, 0.242), (3.100, 0.237),
    #     (3.200, 0.231), (3.300, 0.226), (3.400, 0.221), (3.500, 0.215), (3.600, 0.211), (3.700, 0.206), (3.800, 0.202),
    #     (3.900, 0.198), (4.000, 0.194), (4.200, 0.186), (4.400, 0.179), (4.600, 0.173), (4.800, 0.167), (5.000, 0.162)
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
    # speed_of_sound = 340
    # R = 8.31446262
    # y = 7 / 5
    # tk0 = 273.15
    # tc = 26
    # tf = tc * 9 / 5 + 32
    # pmmrtst = 760
    # patm = pmmrtst / 760
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
                 df_type: Iterable[tuple[float, float]] = None,
                 atmo: tuple[float, float, float] = None):
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
    def df_type(self) -> Iterable[tuple[float, float]]:
        return self._df_type

    @df_type.setter
    def df_type(self, value: Iterable[tuple[float, float]]):
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
                self.calculate_drag_function_multi_bc()

    def sectional_density(self) -> float:
        """ params:
            w: weight in pounds
            d: diameter in inches
        """
        return self._width / (self._diameter ** 2)

    def form_factor_by_bullet_data(self, bc):
        return round(self.sectional_density() / 7000 / bc, 4)

    @staticmethod
    def counted_drag_coefficient(i, cd_def):
        return round(cd_def * i, 4)

    def calculate_drag_function(self):
        i = self.form_factor_by_bullet_data(self._bc, )
        drag_function = []
        for v, cd_def in self._df_type:
            cd = self.counted_drag_coefficient(i, cd_def)
            drag_function.append((v, cd))
        self._df_data = drag_function

    def calculate_drag_function_multi_bc(self):
        i_table = []
        for bc, v in self._bc:
            i_table.append((self.form_factor_by_bullet_data(bc), v))

        drag_function = []

        for idx, (i, vm) in enumerate(i_table):

            for v, cd_def in self._df_type:

                # if len(i_table) > idx > 0 and (i_table[idx - 1][1] > v * self._speed_of_sound > vm):
                #     cd = self.counted_drag_coefficient(i, cd_def)
                #     drag_function.append((v, cd))
                # if idx == 0 and (v * self._speed_of_sound > vm):
                #     cd = self.counted_drag_coefficient(i, cd_def)
                #     drag_function.append((v, cd))
                # if idx == len(i_table) - 1 and i_table[idx][1] > v * self._speed_of_sound > 0:
                #     cd = self.counted_drag_coefficient(i, cd_def)
                #     drag_function.append((v, cd))

                if idx == 0 and v * self._speed_of_sound > i_table[idx + 1][1]:
                    cd = self.counted_drag_coefficient(i, cd_def)
                    drag_function.append((v, cd))

                if idx == len(i_table) - 1 and i_table[idx][1] > v * self._speed_of_sound >= 0:
                    cd = self.counted_drag_coefficient(i, cd_def)
                    drag_function.append((v, cd))


        drag_function.sort()
        self._df_data = drag_function

        # @staticmethod
        # def bc_by_retardation(r_def: float, r: float) -> float:
        #     """ params:
        #         r_def: замедление стандартной пули
        #         r: замедление тестируемой пули
        #     """
        #     return r_def / r

        # @staticmethod
        # def bc_by_form_factor(sd: float = None, w: float = None, d: float = None, i: float = None) -> float:
        #     """ params:
        #         sd: sectional density
        #         w: weight in pounds
        #         d: diameter in inches
        #         i: drag-coefficient
        #     """
        #     if sd and i:
        #         return sd / i
        #     elif w and d and i:
        #         return w / (i * d ** 2)
        #     else:
        #         raise ValueError(f'some arguments are wrong {locals()}')

        # def retardation(self, **kwargs):
        #     """ params:
        #         r_def: замедление стандартной пули
        #         r: замедление тестируемой пули, футы/сек2
        #         v: скорость тестируемой пули, футы/сек
        #         m: степень
        #         A: константа
        #         BC: баллистический коэффициент
        #         p: сила сопротивления воздуха
        #         g: гравитационная константа
        #
        #         r_def = a * v ** m = bc * r = pg
        #         r = a * v ** m / bc
        #     """
        #
        #     return


def main():
    calc = Calculator(w=90, d=0.243, bc=0.218,
                      df_type=DragFunctions.G7, atmo=(15., 760, 50))

    # calc = Calculator(w=90, d=0.243, bc=0.218,
    #                   df_type=DragFunctions.G1, atmo=(15., 760, 50))
    # print(calc.df_data)

    for i, (v, cd) in enumerate(calc.df_data):
        print(round(v, 4), round(cd, 4), round(calc.df_type[i][1], 4))

    calc.bc = [(0.218, 750), (0.21, 720), (0.21, 650), (0.203, 600), (0.201, 500)]
    # print()
    # print(calc.df_data)
    return


if __name__ == '__main__':
    main()
