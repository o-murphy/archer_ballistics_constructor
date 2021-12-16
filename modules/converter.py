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
