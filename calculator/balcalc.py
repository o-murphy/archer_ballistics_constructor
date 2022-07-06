from modules import State
from py_ballisticcalc.extended.profile_extended import *
from py_ballisticcalc.extended.multiple_ballistic_coefficient import MultipleBallisticCoefficient


class EditorProfile(ProfileExtended):

    @property
    def calculated_drag_function(self):
        if self.trajectory_data:
            return self._calculated_drag_function
        return None

    @property
    def distance_step(self):
        return self._distance_step

    @property
    def drag_table(self):
        return self._drag_table

    @property
    def bullet_diameter(self):
        return self._bullet_diameter

    @property
    def bullet_weight(self):
        return self._bullet_weight


class DragEditorState(State):
    def __init__(self, widget, state: dict = None, **kwargs):
        super(DragEditorState, self).__init__(widget, state, **kwargs)

        self.profile = EditorProfile(maximum_distance=(2500, unit.DistanceMeter),
                                     distance_step=(10, unit.DistanceMeter),
                                     sight_angle=(0, 0))

        self.mbc = None

        self.onStateUpdate.connect(self.calculate_trajectory)

    def setProfile(self):
        self.profile._bullet_diameter = unit.Distance(self.diameter, unit.DistanceInch)
        self.profile._bullet_weight = unit.Weight(self.weight, unit.WeightGrain)
        self.profile._bullet_length = unit.Distance(self.length, unit.DistanceInch)
        self.profile._muzzle_velocity = unit.Velocity(self.mv, unit.VelocityMPS)
        self.profile._pressure = unit.Pressure(self.z_pressure, unit.PressureMmHg)
        self.profile._temperature = unit.Temperature(self.z_temp, unit.TemperatureCelsius)
        self.profile._humidity = self.z_humidity
        self.profile._zero_distance = unit.Distance(self.z_d, unit.DistanceMeter)
        self.profile._twist = unit.Distance(self.twist, unit.DistanceInch)
        self.profile._twist_direction = 1 if self.rightTwist else 2
        self.profile._sight_height = unit.Distance(self.sh, unit.DistanceMillimeter)

        if self.df_type in ['G1', 'G1 Multi-BC']:

            if isinstance(self.df_data, float):
                self.profile._drag_table = DragTableG1
                self.profile._bc_value = self.df_data

            elif isinstance(self.df_data, list):
                self.mbc = MultipleBallisticCoefficient(
                    self.df_data, unit.VelocityMPS,
                    DragTableG1,
                    self.profile.bullet_diameter,
                    self.profile.bullet_weight
                )
                self.profile._drag_table = 0
                self.profile._bc_value = 0
                self.profile._custom_drag_function = self.mbc.calculate_custom_drag_func()

        elif self.df_type in ['G7', 'G1 Multi-BC']:

            if isinstance(self.df_data, float):
                self.profile._drag_table = DragTableG7
                self.profile._bc_value = self.df_data

            elif isinstance(self.df_data, list):
                self.mbc = MultipleBallisticCoefficient(
                    self.df_data, unit.VelocityMPS,
                    DragTableG7,
                    self.profile.bullet_diameter,
                    self.profile.bullet_weight
                )
                self.profile._drag_table = 0
                self.profile._bc_value = 0
                self.profile._custom_drag_function = self.mbc.calculate_custom_drag_func()

        elif self.df_type in ['Custom']:
            self.profile._drag_table = 0
            self.profile._bc_value = 0
            self.profile._custom_drag_function = self.df_data

    @property
    def sound_speed(self):
        atmosphere = Atmosphere.create_icao(self.profile._altitude)
        density, mach = atmosphere.get_density_factor_and_mach_for_altitude(0)
        return unit.Velocity(mach, unit.VelocityFPS)

    def calculate_trajectory(self):
        self.setProfile()
        self.profile.calculate_trajectory()
        return self.profile.trajectory_data

    def calculated_drag_function(self):
        if self.profile.trajectory_data:
            return self.profile.calculated_drag_function
        return None

    def get_calculated_drop(self):
        if self.profile.trajectory_data:
            drop = [(p.travelled_distance, p.drop) for p in self.profile.trajectory_data]
            return drop
        return None

    def _trajectory_by_distance_filter(self, point: TrajectoryData, distance: unit.Distance):
        if 0 <= math.fabs(point.travelled_distance.v - distance.v) <= self.profile.distance_step.v / 2:
            return point
        else:
            return None

    def get_trajectory_data_at_distance(self, distance: unit.Distance):
        if self.profile.trajectory_data:
            points = filter(lambda p: self._trajectory_by_distance_filter(p, distance), self.profile.trajectory_data)
            points_li = list(points)
            if points_li:
                return points_li[0]
        return None

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
