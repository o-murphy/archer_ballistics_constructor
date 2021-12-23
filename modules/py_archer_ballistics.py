from bin import archer_ballistics


"""
    'qt_spinbox_lineedit', 'tileBulletWeight', 'rifleName', 'caliberName', 'caliberShort', 'twistSpinBox', 
    'shSpinBox', 'rightTwist', 'leftTwist', 'cartridgeName', 'mvComboBox', 'tsDoubleSpinBox', 'mvSpinBox', 
    'temperatureSpinBox', 'bulletName', 'weightComboBox', 'lengthComboBox', 'diameterComboBox', 'dragComboBox', 
    'bulletWeight', 'lengthDoubleSpinBox', 'diameterDoubleSpinBox', 'bcDoubleSpinBox'
"""


def rnd4(val: float) -> float:
    return round(val, 4)


class Params(object):
    def __init__(self, params):
        self.params = params


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
    def __init__(self, params):
        super().__init__(params)
        self.Temperature = self.params['z_temp']
        self.P_Temperature = self.params['z_powder_temp']
        self.Humidity = self.params['z_humidity']
        self.Pressure = self.params['z_pressure']
        self.Angle = self.params['z_angle']
        self.Azimuth = self.params['z_azimuth']
        self.Latitude = self.params['z_latitude']


class Bullet(Params):
    """ params:
            bc       :   Ballistic Coefficient List
            diameter :   Bullet Diameter
            length   :   Bullet Length
            weight   :   Bullet Weight
            dragType :   Drag Func Type
    """

    def __init__(self, params):
        super().__init__(params)
        self.DragFunc = self.set_drag_func_type()
        # self.BalCoef = self.params['bc']
        self.BalCoef = None
        self.BVelocity = None
        self.Diameter = self.params['diameter']
        self.Length = self.params['length']
        self.Weight = self.params['weight']
        self.set_bc()

    def set_drag_func_type(self):
        drag_func_type = [1, 7, 11, 17, 10]
        return drag_func_type[self.params['dragType']]

    def set_bc(self):
        self.BalCoef = [0.0] * 5
        self.BVelocity = [-1] * 5
        self.BalCoef[0] = 0.3
        self.BVelocity[0] = 800


class Cartridge(Params):
    """ params:
        mv      :   Muzzle velocity
        temp    :   Temperature on muzzle velocity
        ts      :   Powder temperature sensitivity
    """

    def __init__(self, params):
        super().__init__(params)
        self.V0 = int(self.params['mv'])
        self.T0 = int(self.params['temp'])
        self.PowderSens = self.params['ts']


class Barrel(Params):
    """ params:
        SightHeight   :   Sight height
        Zero          :   Zero distance
        Twist         :   Barrel twist
        H_zero        :   Zeroing H
        V_zero        :   Zeroing V
        rightTwist    :   is right twist
    """

    def __init__(self, params):
        super().__init__(params)
        self.SightHeight = int(self.params['sh'])
        self.Zero = int(self.params['z_d'])
        self.H_zero = int(self.params['z_x'] * 4)
        self.V_zero = int(self.params['z_y'] * 4)
        self.twist_value = self.params['rightTwist']
        self.is_right = self.params['rightTwist']
        self.Twist = self.set_twist()

    def set_twist(self):
        return self.twist_value if self.is_right else -self.twist_value


class Profile(Conditions, Bullet, Cartridge, Barrel):
    def __init__(self, params):
        super().__init__(params)


class ArcherBallistics(object):
    def __init__(self):
        self.ballistics = archer_ballistics
        self.drag_function = None
        self.drop_at_distance = None
        self.cd_at_distance = None
        self.atmo = None
        self.sound_speed = None

    def set_drag_function(self, drag_function_data: list):
        self.drag_function = []
        [[self.drag_function.append(j) for j in i] for i in drag_function_data[::-1]]
        self.ballistics.set_drag_function(self.drag_function)

    def get_drop_at_distance(self, distances: list):
        self.drop_at_distance = self.ballistics.get_drop_at_distance(distances)

    def get_cd_at_distance(self, distance: list = None):
        self.cd_at_distance = rnd4(self.ballistics.get_cd_at_distance(distance))

    def calculate_drop(self, drag_function: list = None, distances: list = None) -> list:
        if drag_function:
            self.set_drag_function(drag_function)
        self.get_drop_at_distance(distances)
        return self.drop_at_distance

    def calculate_cd(self, drag_function: list = None, distance: float = None) -> float:
        if drag_function:
            self.set_drag_function(drag_function)
        self.get_cd_at_distance(distance)
        return self.cd_at_distance

    def set_atmo(self, conditions: Conditions):
        self.atmo = conditions
        if self.atmo:
            return self.ballistics.set_atmo(self.atmo)

    def get_atmo(self):
        return self.ballistics.get_atmo() if self.atmo else None

    def get_sound_speed(self):
        if self.atmo:
            self.sound_speed = self.ballistics.get_speed_of_sound()
        return self.sound_speed

    def set_profile(self, profile: Profile):
        if profile:
            return self.ballistics.set_profile(profile)

    def get_profile(self):
        return self.ballistics.get_profile()

    def get_drag_function(self):
        return self.ballistics.get_drag_function()


if __name__ == '__main__':
    print()
    # test_data = {'z_d': 100, 'z_y': 0, 'z_x': 0, 'rifleName': '', 'caliberName': '.223 Remington', 'sh': 90, 'twist': 10, 'caliberShort': '.233Rem', 'rightTwist': True, 'bulletName': '', 'weight': 69.0, 'length': 0.9, 'diameter': 0.224, 'weightTile': '69gr', 'dragType': 1, 'bc': 0.169, 'cartridgeName': '', 'mv': 868, 'temp': 15, 'ts': 1.55, 'z_temp': 15, 'z_angle': 0, 'z_pressure': 760, 'z_latitude': 0, 'z_humidity': 50, 'z_azimuth': 270, 'z_powder_temp': 15}
    #
    # calc = ArcherBallistics()
    #
    # profile = Profile(test_data)
    #
    # archer_ballistics.set_profile(profile)
    # print(archer_ballistics.get_drag_function())
