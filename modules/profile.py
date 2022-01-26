from PyQt5 import QtCore


class BProfile(QtCore.QObject):

    setter = QtCore.pyqtSignal(object, object)

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.installEventFilter(self)
        # self.setter.connect(self.customEv)

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __setattr__(self, key, value):
        self.setter.emit(key, value)
        super().__setattr__(key, value)


    def customEv(self, key, value):
        print(key, value)
        pass


class Conditions(object):
    def __init__(self, z_temp=None, z_powder_temp=None, z_humidity=None, z_pressure=None, z_angle=None,
                 z_azimuth=None, z_latitude=None):
        self.Temperature = z_temp
        self.P_Temperature = z_powder_temp
        self.Humidity = z_humidity
        self.Pressure = z_pressure
        self.Angle = z_angle
        self.Azimuth = z_azimuth
        self.Latitude = z_latitude


class Bullet(object):
    def __init__(self, drag_type: int = None, diameter=None, length=None, weight=None,
                 is_mbc=False, bc=None, mv=None, mbc=None, df_data=None):
        self.is_mbc = is_mbc
        self.mbc = mbc
        self.bc = bc
        self.mv = mv
        self.dragType = drag_type
        self.DragFunc = self.set_drag_func_type()
        self.BalCoef = []
        self.BVelocity = []
        self.Diameter = diameter
        self.Length = length
        self.Weight = weight
        self.set_bc()
        self.df_data = df_data

    def set_drag_func_type(self):
        drag_func_type = [1, 7, 10]
        if self.is_mbc:
            drag_func_type = [11, 17, 10]
        return drag_func_type[self.dragType]

    def set_bc(self):
        self.BalCoef = [0.0] * 5
        self.BVelocity = [-1] * 5

        if self.is_mbc:
            for i, (v, bc) in enumerate(self.mbc):
                if bc > 0 and v >= 0:
                    self.BalCoef[i] = bc
                    self.BVelocity[i] = v
        else:
            self.BalCoef[0] = self.bc
            self.BVelocity[0] = self.mv


class Cartridge(object):
    def __init__(self, mv=None, temp=None, ts=None):
        self.V0 = int(mv) if mv else None
        self.T0 = int(temp) if temp else None
        self.PowderSens = ts


class Barrel(object):
    def __init__(self, name: str = None, caliber_name: str = None, caliber_tile: str = None,
                 sh=None, z_d=None, z_x=None, z_y=None, twist=None, is_right=None):
        self.name = name
        self.caliber_name = caliber_name
        self.caliber_tile = caliber_tile

        self.Zero = int(z_d)
        self.H_zero = int(z_x * 4)
        self.V_zero = int(z_y * 4)

        self.SightHeight = int(sh)
        self.twist_value = twist
        self.is_right = is_right
        self.Twist = self.set_twist()

    def set_twist(self):
        return self.twist_value if self.is_right else -self.twist_value


class Profile(object):
    def __init__(self):
        self.barrel = Barrel()
        self.cartridge = Cartridge()
        self.bullet = Bullet()
        self.conditions = Conditions()
