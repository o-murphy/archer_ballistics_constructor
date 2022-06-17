from typing import Callable, Iterator, Union, Optional
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
    G7 = (
        (0.000, 0.120), (0.050, 0.120), (0.100, 0.120), (0.150, 0.119), (0.200, 0.119), (0.250, 0.119), (0.300, 0.119),
        (0.350, 0.119), (0.400, 0.119), (0.450, 0.119), (0.500, 0.119), (0.550, 0.119), (0.600, 0.119), (0.650, 0.120),
        (0.700, 0.120), (0.725, 0.121), (0.750, 0.122), (0.775, 0.123), (0.800, 0.124), (0.825, 0.127), (0.850, 0.131),
        (0.875, 0.137), (0.900, 0.146), (0.925, 0.166), (0.950, 0.205), (0.975, 0.299), (1.000, 0.380), (1.025, 0.402),
        (1.050, 0.404), (1.075, 0.403), (1.100, 0.401), (1.125, 0.399), (1.150, 0.396), (1.200, 0.388), (1.250, 0.381),
        (1.300, 0.373), (1.350, 0.366), (1.400, 0.358), (1.500, 0.344), (1.550, 0.338), (1.600, 0.332), (1.650, 0.326),
        (1.700, 0.321), (1.750, 0.316), (1.800, 0.312), (1.850, 0.308), (1.900, 0.304), (1.950, 0.301), (2.000, 0.298),
        (2.050, 0.295), (2.100, 0.292), (2.150, 0.289), (2.200, 0.286), (2.250, 0.283), (2.300, 0.281), (2.350, 0.278),
        (2.400, 0.275), (2.450, 0.273), (2.500, 0.270), (2.550, 0.267), (2.600, 0.264), (2.650, 0.262), (2.700, 0.259),
        (2.750, 0.256), (2.800, 0.253), (2.850, 0.251), (2.900, 0.248), (2.950, 0.245), (3.000, 0.242), (3.100, 0.237),
        (3.200, 0.231), (3.300, 0.226), (3.400, 0.221), (3.500, 0.215), (3.600, 0.211), (3.700, 0.206), (3.800, 0.202),
        (3.900, 0.198), (4.000, 0.194), (4.200, 0.186), (4.400, 0.179), (4.600, 0.173), (4.800, 0.167), (5.000, 0.162)
    )


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
                 df_type: Iterator[tuple[float, float]] = None,
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
    def df_type(self) -> Iterator[tuple[float, float]]:
        return self._df_type

    @df_type.setter
    def df_type(self, value: Iterator[tuple[float, float]]):
        self._df_type = value
        self.calculate_df()

    @property
    def df_data(self) -> Iterator[tuple[float, int]]:
        return self._df_data

    @df_data.setter
    def df_data(self, value: Iterator[tuple[float, float]]):
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

                if len(i_table) > idx > 0 and (i_table[idx - 1][1] > v * self._speed_of_sound > vm):
                    cd = self.counted_drag_coefficient(i, cd_def)
                    drag_function.append((v, cd))
                if idx == 0 and (v * self._speed_of_sound > vm):
                    cd = self.counted_drag_coefficient(i, cd_def)
                    drag_function.append((v, cd))
                if idx == len(i_table) - 1 and i_table[idx][1] > v * self._speed_of_sound > 0:
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
                      df_type=DragFunctions.G7, atmo=(26., 101.325, 50))
    print(calc.df_data)
    calc.bc = [(0.218, 750), (0.21, 720), (0.21, 650), (0.203, 600), (0.201, 500)]
    print(calc.df_data)
    return


if __name__ == '__main__':
    main()
