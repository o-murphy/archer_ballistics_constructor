from bin import archer_ballistics


"""
    'qt_spinbox_lineedit', 'tileBulletWeight', 'rifleName', 'caliberName', 'caliberShort', 'twistSpinBox', 
    'shSpinBox', 'rightTwist', 'leftTwist', 'cartridgeName', 'mvComboBox', 'tsDoubleSpinBox', 'mvSpinBox', 
    'temperatureSpinBox', 'bulletName', 'weightComboBox', 'lengthComboBox', 'diameterComboBox', 'dragComboBox', 
    'bulletWeight', 'lengthDoubleSpinBox', 'diameterDoubleSpinBox', 'bcDoubleSpinBox'
"""


def rnd4(val: float) -> float:
    return round(val, 4)


class ArcherBallistics(object):
    def __init__(self):
        self.ballistics = archer_ballistics
        self.drop_at_distance = None
        self.cd_at_distance = None

    def set_drag_function(self, drag_function: list):
        drag_function_data = []
        [[drag_function_data.append(j) for j in i] for i in drag_function[::-1]]
        self.ballistics.set_drag_function(drag_function_data)

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
        print(self.cd_at_distance)
        return self.cd_at_distance

    def set_atmo(self):
        archer_ballistics.set_atmo(atmo)


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
        # self.Pressure = self.params['z_pressure']
        self.Angle = self.params['z_angle']
        self.Azimuth = self.params['z_azimuth']
        self.Latitude = self.params['z_latitude']


class Bullet(Params):
    """ params:
            bcDoubleSpinBox       :   Ballistic Coefficient
            diameterDoubleSpinBox :   Bullet Diameter
            lengthDoubleSpinBox   :   Bullet Length
            weightComboBox        :   Bullet Weight
            dragComboBox          :   Drag Func Type
    """

    def __init__(self, params):
        super().__init__(params)
        self.DragFunc = self.set_drag_func_type()
        self.BalCoef = self.params['bcDoubleSpinBox']
        self.Diameter = self.params['diameterDoubleSpinBox']
        self.Length = self.params['lengthDoubleSpinBox']
        self.Weight = self.params['weightComboBox']

    def set_drag_func_type(self):
        drag_func_type = [1, 7, 11, 17, 10]
        return drag_func_type[self.params['dragComboBox']]


class Cartridge(Params):
    """ params:
        mvSpinBox             :   Muzzle velocity
        temperatureSpinBox    :   Temperature on muzzle velocity
        tsDoubleSpinBox       :   Powder temperature sensitivity
    """

    def __init__(self, params):
        super().__init__(params)
        self.V0 = self.params['mvSpinBox']
        self.T0 = self.params['temperatureSpinBox']
        self.PowderSens = self.params['tsDoubleSpinBox']


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
        self.SightHeight = self.params['shSpinBox']
        self.Zero = self.params['shSpinBox']
        self.H_zero = self.params['doubleSpinBox_x']
        self.V_zero = self.params['doubleSpinBox_y']
        self.twist_value = self.params['rightTwist']
        self.is_right = self.params['rightTwist']
        self.Twist = self.set_twist()

    def set_twist(self):
        return self.twist_value if self.is_right else -self.twist_value


class Profile(Conditions, Bullet, Cartridge):
    def __init__(self, params):
        super().__init__(params)


if __name__ == '__main__':

    import json
    with open(r"C:\Users\Sergey\Documents\ArcherBC\Recent\recent_21-12-17_17-13-18.json", 'r') as fp:
        cond = json.load(fp)

    atmo = Conditions(cond[0])
    archer_ballistics.set_atmo(atmo)
    # print(archer_ballistics.get_atmo())
    #
    # print(archer_ballistics.get_speed_of_sound())

    pass
