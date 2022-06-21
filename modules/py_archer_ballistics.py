from bin import archer_ballistics


def rnd4(val: float) -> float:
    return round(val, 4)


class Params(object):
    def __init__(self, params, **kwargs):
        self.params = params
        self.kwargs = kwargs


class Conditions(Params):
    """ params:
        z_temp        :   Atmosphere temperature
        z_powder_temp :   Powder temperature
        z_humidity    :   Humidity
        z_pressure    :   Atmosphere pressure
        z_latitude    :   Latitude
        z_angle       :   Angle
        z_azimuth     :   Azimuth
        z_slope_angle :   Slope Angle
    """

    z_temp = None
    z_powder_temp = None
    z_humidity = None
    z_pressure = None
    z_angle = None
    z_azimuth = None
    z_latitude = None

    def __init__(self, params, **kwargs):
        super().__init__(params, **kwargs)
        if params:
            kwargs.update(params)
        [self.__setattr__(k, v) for k, v in kwargs.items()]
        self.Temperature = self.z_temp
        self.P_Temperature = self.z_powder_temp
        self.Humidity = self.z_humidity
        self.Pressure = self.z_pressure
        self.Angle = self.z_angle
        self.Azimuth = self.z_azimuth
        self.Latitude = self.z_latitude


class Bullet(Params):
    """ params:
        bc       :   Ballistic Coefficient List
        diameter :   Bullet Diameter
        length   :   Bullet Length
        weight   :   Bullet Weight
        dragType :   Drag Func Type
    """

    diameter = None
    length = None
    weight = None
    df_type = None
    df_data = None

    mv = None

    def __init__(self, params, **kwargs):
        super().__init__(params, **kwargs)

        if params:
            kwargs.update(params)
        [self.__setattr__(k, v) for k, v in kwargs.items()]

        self.DragFunc = self.set_drag_func_type()

        # self.df_data = self.df_data
        self.BalCoef = None
        self.BVelocity = None
        self.Diameter = self.diameter
        self.Length = self.length
        self.Weight = self.weight
        self.set_bc()
        # self.df_data = self.params['df_data'] if 'df_data' in self.params else None

    def set_drag_func_type(self):
        drag_func_type = {
            'G1': 11,
            'G7': 17,
            'G1 Multi-BC': 11,
            'G7 Multi-BC': 17,
            'Custom': 10
        }
        return drag_func_type[self.df_type]

    def set_bc(self, mbc=None):
        self.BalCoef = [-1] * 5
        self.BVelocity = [-1] * 5
        if self.DragFunc == 10:
            self.df_data = self.df_data
        if self.DragFunc in [11, 17, 1, 7]:
            if isinstance(self.df_data, float or int):
                self.BalCoef[0], self.BVelocity[0] = self.df_data, self.mv
            elif isinstance(self.df_data, list or tuple):
                for i, (bc, v) in enumerate(self.df_data):
                    if bc > 0 and v >= 0:
                        self.BalCoef[i] = bc
                        self.BVelocity[i] = v


class Cartridge(Params):
    """ params:
        mv      :   Muzzle velocity
        temp    :   Temperature on muzzle velocity
        ts      :   Powder temperature sensitivity
    """

    mv = None
    temp = None
    ts = None

    def __init__(self, params, **kwargs):
        super().__init__(params, **kwargs)

        if params:
            kwargs.update(params)
        [self.__setattr__(k, v) for k, v in kwargs.items()]

        self.V0 = int(self.mv)
        self.T0 = int(self.temp)
        self.PowderSens = self.ts


class Barrel(Params):
    """ params:
        SightHeight   :   Sight height
        Zero          :   Zero distance
        Twist         :   Barrel twist
        H_zero        :   Zeroing H
        V_zero        :   Zeroing V
        rightTwist    :   is right twist
    """

    sh = None
    z_d = None
    z_x = None
    z_y = None
    twist = None
    rightTwist = None
    Twist = None

    def __init__(self, params, **kwargs):
        super().__init__(params, **kwargs)

        if params:
            kwargs.update(params)
        [self.__setattr__(k, v) for k, v in kwargs.items()]

        self.SightHeight = int(self.sh)
        self.Zero = int(self.z_d)
        self.H_zero = int(self.z_x * 4)
        self.V_zero = int(self.z_y * 4)
        self.twist_value = self.twist
        self.is_right = self.rightTwist
        self.set_twist()

    def set_twist(self):
        self.Twist = self.twist_value if self.is_right else -self.twist_value


class Profile(Conditions, Bullet, Cartridge, Barrel):
    def __init__(self, params, **kwargs):
        super().__init__(params, **kwargs)


class ArcherBallistics(object):
    def __init__(self):
        self.ballistics = archer_ballistics

    @property
    def drag_function(self):
        ret = self.ballistics.get_drag_function()
        table = ''
        for (v, c) in ret:
            table += str(v) + '\t' + str(c) + '\n'
        ret.sort(reverse=False)
        return ret

    @drag_function.setter
    def drag_function(self, drag_function_data: list):
        drag_function_data.sort(reverse=True)
        drag_function = []
        [[drag_function.append(j) for j in i] for i in drag_function_data]
        self.ballistics.set_drag_function(drag_function)

    def get_drop_at_distance(self, distances: list):
        return self.ballistics.get_drop_at_distance(distances)

    def get_cd_at_distance(self, distance: list = None):
        return rnd4(self.ballistics.get_cd_at_distance(distance))

    def calculate_drop(self, distances: list = None) -> list:
        # if drag_function:
        #     self.drag_function = drag_function
        return self.get_drop_at_distance(distances)

    def calculate_cd(self, drag_function: list = None, distance: float = None) -> float:
        if drag_function:
            self.drag_function = drag_function
        return self.get_cd_at_distance(distance)

    def get_sound_speed(self):
        return self.ballistics.get_speed_of_sound()

    @property
    def profile(self):
        return self.ballistics.get_profile()

    @profile.setter
    def profile(self, profile: Profile):
        if profile:
            self.ballistics.set_profile(profile)

    @property
    def atmo(self):
        return self.ballistics.get_atmo()

    @atmo.setter
    def atmo(self, value):
        self.ballistics.set_atmo(value)


if __name__ == '__main__':
    test_data = {
        "SightHeight": 90,
        "Zero": 100,
        "H_zero": 0,
        "V_zero": 0,
        "twist_value": 11,
        "is_right": True,
        "Twist": 11,
        "V0": 800,
        "T0": 15,
        "PowderSens": 1.55,
        "DragFunc": 1,
        "BalCoef": [
            0.547,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        "BVelocity": [
            800,
            -1,
            -1,
            -1,
            -1
        ],
        "Diameter": 0.308,
        "Length": 1.3,
        "Weight": 150.0,
        "Temperature": 15,
        "P_Temperature": 15,
        "Humidity": 50,
        "Pressure": 760,
        "Angle": 0,
        "Azimuth": 270,
        "Latitude": 0
    }
