from modules import State
from modules import ArcherBallistics, Profile


class DragEditorState(State):
    def __init__(self, widget, state: dict = None, **kwargs):
        super(DragEditorState, self).__init__(widget, state, **kwargs)

        self.ballistics = ArcherBallistics()
        self.profile = Profile(self.__dict__)

        self.setProfile()
        self.sound_speed = self.get_sound_speed()
        print(self.sound_speed)

    @property
    def drag_function(self):
        return self.ballistics.drag_function

    @drag_function.setter
    def drag_function(self, drag_function):
        self.ballistics.drag_function = drag_function

    @property
    def calculate_drop(self):
        return self.ballistics.calculate_drop(self.default_drag_func, self.distances)

    def get_sound_speed(self):
        return self.ballistics.get_sound_speed()

    def drop_at_distance(self):
        return self.ballistics.get_drop_at_distance(self.distances)

    def get_cd_at_distance(self, distance):
        return self.ballistics.get_cd_at_distance(distance)

    def calculate_cd(self, drag_function: list = None, distance: float = None):
        return self.ballistics.calculate_cd(drag_function, distance)

    @staticmethod
    def distances_generator():
        return [i for i in range(25, 2500, 25)]

    def setProfile(self):
        self.ballistics.profile = self.profile
        if self.profile.DragFunc == 10 and self.profile.df_data:
            self.ballistics.drag_function = self.profile.df_data
        self.ballistics.atmo = self.profile
        self.ballistics.get_sound_speed()

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
