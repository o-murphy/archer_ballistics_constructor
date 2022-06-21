from modules import State
from modules import ArcherBallistics, Profile
from calculator import Calculator, DragFunctions


class DragEditorState(State):
    def __init__(self, widget, state: dict = None, **kwargs):
        super(DragEditorState, self).__init__(widget, state, **kwargs)

        self.profile = None
        self.ballistics = ArcherBallistics()
        self.setProfile()
        self.sound_speed = self.get_sound_speed()

        # self.calculator = Calculator(w=self.weight, d=self.diameter, bc=self.df_data,
        #                              df_type=DragFunctions.G7,
        #                              atmo=(self.z_temp, self.z_pressure, self.z_humidity))

        self.calculator = Calculator(w=self.weight, d=self.diameter, bc=self.df_data,
                                     df_type=DragFunctions.G7,
                                     atmo=(self.z_temp, self.z_pressure, self.z_humidity))

        print(f'\n\nMy\n')

        for i in self.calculator.df_data:
            print(i[1])

        print(f'\n\nDef\n')

        for i in self.drag_function:
            print(i[1])

        print()

        # from calculator.calculator import Constant
        # self.sound_speed = Constant.speed_of_sound(self.z_temp, self.z_pressure, self.z_humidity)

    def setProfile(self):
        self.profile = Profile(self.__dict__)
        self.ballistics.profile = self.profile
        self.ballistics.atmo = self.profile

    @property
    def drag_function(self):
        return self.ballistics.drag_function

    @drag_function.setter
    def drag_function(self, drag_function):
        self.ballistics.drag_function = drag_function

    def calculate_drop(self, drag_function):
        return self.ballistics.calculate_drop(self.distances)

    def calculate_drop_on_distance(self, distance):
        drop = self.ballistics.calculate_drop([distance])[0]
        return drop

    def get_sound_speed(self):
        return self.ballistics.get_sound_speed()

    def drop_at_distances(self):
        return self.ballistics.get_drop_at_distance(self.distances)

    def get_cd_at_distance(self, distance):
        return self.ballistics.get_cd_at_distance(distance)

    def calculate_cd(self, drag_function: list = None, distance: float = None):
        return self.ballistics.calculate_cd(drag_function, distance)

    @staticmethod
    def distances_generator():
        return [i for i in range(25, 2500, 25)]

    @staticmethod
    def namestr(obj, namespace):
        return [name for name in namespace if namespace[name] is obj]

    def updateState(self, state: dict = None, *args, **kwargs):
        super().updateState(state, *args, **kwargs)

    default_drag_func = None
    current_drag_func = None
    distances = None
    current_distance = None
    default_drop = None
    current_drop = None
    rifleName = 'Template'
    caliberName = '.308 Win'
    sh = 90
    twist = 11
    caliberShort = ''
    rightTwist = True
    bulletName = 'Hornady ELD Match'
    weight = 178.0
    length = 1.3
    diameter = 0.308
    weightTile = '178gr'
    drags = []
    drag_idx = -1
    cartridgeName = 'Template'
    mv = 800
    temp = 15
    ts = 1.55
    z_pressure = 760
    z_angle = 0
    z_temp = 15
    z_humidity = 50
    z_azimuth = 270
    z_latitude = 0
    z_powder_temp = 15
    z_d = 100
    z_x = 0.0
    z_y = 0.0
    df_data = None
    df_type = 'Custom'
    df_comment = 'Empty'


if __name__ == '__main__':
    try:
        from .defaults import EXAMPLE_G1
    except ImportError as err:
        from gui.drag_func_editor.defaults import EXAMPLE_G7

    from PyQt5 import QtWidgets


    class W(QtWidgets.QWidget):
        def __init__(self):
            super(W).__init__()
            self.state = DragEditorState(self, EXAMPLE_G7)


    wid = W()
    # print(wid.state.__dict__)
    print()
    print(wid.state.drag_function[40])
    print(wid.state.ballistics.profile)

    wid.state.weight = 100
    wid.state.z_temp = 26
    wid.state.df_data = 0.3

    wid.state.profile = Profile(wid.state.__dict__)
    wid.state.setProfile()

    print()
    print(wid.state.drag_function[40])
    print(wid.state.ballistics.profile)
