import math


class Calculator(object):
    def __init__(self):
        pass

    @staticmethod
    def bc_by_retardation(r_def: float, r: float) -> float:
        """ params:
            r_def: замедление стандартной пули
            r: замедление тестируемой пули
        """
        return r_def / r

    @staticmethod
    def bc_by_form_factor(sd: float = None, w: float = None, d: float = None, i: float = None) -> float:
        """ params:
            sd: sectional density
            w: weight in pounds
            d: diameter in inches
            i: drag-coefficient
        """
        if sd and i:
            return sd / i
        elif w and d and i:
            return w / (i * d ** 2)
        else:
            raise ValueError(f'some arguments are wrong {locals()}')

    @staticmethod
    def sectional_density(w: float, d: float) -> float:
        """ params:
            w: weight in pounds
            d: diameter in inches
        """
        return w / (d ** 2)

    def retardation(self, **kwargs):
        """ params:
            r_def: замедление стандартной пули
            r: замедление тестируемой пули, футы/сек2
            v: скорость тестируемой пули, футы/сек
            m: степень
            A: константа
            BC: баллистический коэффициент
            p: сила сопротивления воздуха
            g: гравитационная константа

            r_def = a * v ** m = bc * r = pg
            r = a * v ** m / bc
        """

        return


def main():
    calc = Calculator()
    calc.retardation(r_def = 1, r = 3, c = 4)

    return


if __name__ == '__main__':
    main()
