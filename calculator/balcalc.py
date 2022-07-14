from modules import State
# from py_ballisticcalc.extended.profile_extended import *
# from py_ballisticcalc.extended.multiple_ballistic_coefficient import MultipleBallisticCoefficient

from py_ballisticcalc.lib.profile import Profile
from py_ballisticcalc.lib.bmath.unit import *
from py_ballisticcalc.lib.drag import DragTableG1, DragTableG7
from py_ballisticcalc.lib.weapon import TwistRight, TwistLeft
from py_ballisticcalc.lib.trajectory_calculator import TrajectoryData
from py_ballisticcalc.lib.atmosphere import Atmosphere, IcaoAtmosphere

import math


# class EditorProfile(ProfileExtended):
#
#     @property
#     def calculated_drag_function(self):
#         if self.trajectory_data:
#             return self._calculated_drag_function
#         return None
#
#     @property
#     def distance_step(self):
#         return self._distance_step
#
#     @property
#     def drag_table(self):
#         return self._drag_table
#
#     @property
#     def bullet_diameter(self):
#         return self._bullet_diameter
#
#     @property
#     def bullet_weight(self):
#         return self._bullet_weight


class DragEditorState(State):
    def __init__(self, widget, state: dict = None, **kwargs):
        super(DragEditorState, self).__init__(widget, state, **kwargs)

        # self.profile = EditorProfile(maximum_distance=(2500, unit.DistanceMeter),
        #                              distance_step=(1, unit.DistanceMeter),
        #                              sight_angle=(0, 0),
        #                              maximum_step_size=(5, unit.DistanceFoot)
        #                              )

        self.profile = None

        self.mbc = None

        self.onStateUpdate.connect(self.calculate_trajectory)

    def setProfile(self):

        custom_df = []
        mbc = []
        bc_value = 0
        drag_table = DragTableG1

        if self.df_type in ['G1', 'G1 Multi-BC']:

            if isinstance(self.df_data, float):
                drag_table = DragTableG1
                bc_value = self.df_data

            elif isinstance(self.df_data, list):
                drag_table = DragTableG1
                bc_value = 0
                custom_df = []
                mbc = self.mbc

        if self.df_type in ['G7', 'G7 Multi-BC']:

            if isinstance(self.df_data, float):
                drag_table = DragTableG7
                bc_value = self.df_data

            elif isinstance(self.df_data, list):
                drag_table = DragTableG7
                bc_value = 0
                custom_df = []
                mbc = self.mbc

        self.profile = Profile(
            bc_value=bc_value,
            custom_drag_function=custom_df,
            multiple_bc_table=mbc,
            maximum_distance=(2500, DistanceMeter),
            distance_step=(1, DistanceMeter),
            sight_angle=(0, 0),
            maximum_step_size=(5, DistanceFoot),
            bullet_diameter=(self.diameter, DistanceInch),
            bullet_weight=(self.weight, WeightGrain),
            bullet_length=(self.length, DistanceInch),
            muzzle_velocity=(self.mv, VelocityMPS),
            pressure=(self.z_pressure, PressureMmHg),
            temperature=(self.z_temp, TemperatureCelsius),
            humidity=self.z_humidity,
            zero_distance=(self.z_d, DistanceMeter),
            twist=(self.twist, DistanceInch),
            twist_direction=TwistRight if self.rightTwist else TwistLeft,
            sight_height=(self.sh, DistanceMillimeter),
        )

    def sound_speed(self):
        atmosphere = IcaoAtmosphere(Distance(0, DistanceMeter))
        density, mach = atmosphere.get_density_factor_and_mach_for_altitude(0)
        return Velocity(mach, VelocityFPS)

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

    def _trajectory_by_distance_filter(self, point: TrajectoryData, distance: Distance):
        if 0 <= math.fabs(point.travelled_distance.v - distance.v) <= self.profile.distance_step.v / 2:
            return point
        else:
            return None

    def get_trajectory_data_at_distance(self, distance: Distance):
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
