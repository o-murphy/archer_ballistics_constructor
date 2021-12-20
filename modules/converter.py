import math


class BConverter(object):
    def __init__(self):
        pass

    @staticmethod
    def nothing(x, *args):
        return x

    @staticmethod
    def cm2mil(cm, dist):
        return cm/(10*(dist/100))

    @staticmethod
    def cm2moa(cm, dist):
        return cm/(2.91*(dist/100))

    @staticmethod
    def rnd4(val: float) -> float:
        return round(val, 4)

    @staticmethod
    def auto_rnd(val: float) -> float:
        return round(val, 5 - len(str(int(val))))

    @staticmethod
    def inch_to_mm(cur_val):
        return cur_val * 25.4

    @staticmethod
    def mm_to_inch(cur_val):
        return cur_val / 25.4

    @staticmethod
    def gr_to_g(cur_val):
        return round(cur_val * 0.06479891, 2)

    @staticmethod
    def g_to_gr(cur_val):
        return round(cur_val / 0.06479891, 1)

    @staticmethod
    def mps2fps(val):
        return math.ceil(val * 3.28)

    @staticmethod
    def fps2mps(val):
        return math.floor(val / 3.28)
