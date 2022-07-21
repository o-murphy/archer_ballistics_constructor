from modules import State

from py_ballisticcalc.lib.profile import Profile
from py_ballisticcalc.lib.bmath.unit import *
from py_ballisticcalc.lib.drag import DragTableG1, DragTableG7
from py_ballisticcalc.lib.weapon import TwistRight, TwistLeft
from py_ballisticcalc.lib.trajectory_calculator import TrajectoryData
from py_ballisticcalc.lib.atmosphere import Atmosphere, IcaoAtmosphere

import math


class DragEditorState(State):
    def __init__(self, widget, state: dict = None, **kwargs):
        super(DragEditorState, self).__init__(widget, state, **kwargs)

        self.profile = None
        self.trajectory_data = None

        self.mbc = None

        self.onStateUpdate.connect(self.calculate_trajectory)

    def get_df_type_flags(self):
        if self.df_type == 'G1':
            return DragTableG1, False
        elif self.df_type == 'G1 Multi-BC':
            return DragTableG7, True
        if self.df_type == 'G7':
            return DragTableG7, False
        elif self.df_type == 'G7 Multi-BC':
            return DragTableG7, True
        else:
            return 0, False

    def setProfile(self):

        custom_df = []
        drag_table, is_mbc = self.get_df_type_flags()

        if is_mbc and drag_table != 0:
            mbc = self.df_data
            bc_value = 0
        elif not is_mbc and drag_table != 0:
            mbc = []
            bc_value = self.df_data
        else:
            mbc = []
            bc_value = 0
            # if not self.default_drag_func:
            self.default_drag_func = self.df_data
            custom_df = [{'A': p[0], 'B': p[1]} for p in self.default_drag_func]

            if self.current_drag_func:
                custom_df = [{'A': p[0], 'B': p[1]} for p in self.current_drag_func]

            # else:
            #     self.default_drag_func = self.df_data
            #     custom_df = [{'A': p[0], 'B': p[1]} for p in self.default_drag_func]

        self.profile = Profile(
            bc_value=bc_value,
            drag_table=drag_table,
            custom_drag_function=custom_df,
            multiple_bc_table=mbc,
            maximum_distance=(2500, DistanceMeter),
            distance_step=(5, DistanceMeter),
            sight_angle=(0, 0),
            maximum_step_size=(5, DistanceMeter),
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
        try:
            trajectory = self.profile.calculate_trajectory()
            self.trajectory_data = trajectory
            return self.trajectory_data
        except ZeroDivisionError:
            return []

    def calculated_drag_function(self):
        if not self.trajectory_data:
            self.calculate_trajectory()
        try:
            table = self.profile.calculate_drag_table()
            return table
        except ZeroDivisionError:
            return []

    def get_calculated_drop(self):
        if not self.trajectory_data:
            self.calculate_trajectory()
        drop = [(p.travelled_distance(), p.drop()) for p in self.trajectory_data]
        return drop
        # return None

    def _trajectory_by_distance_filter(self, point: TrajectoryData, distance: Distance):
        units = distance.units()
        distance_delta = math.fabs(point.travelled_distance().value(units) - distance.value(units))
        step = self.profile.distance_step().value(units) / 2
        if 0 <= distance_delta <= step:
            return point
        else:
            return None

    def get_trajectory_data_at_distance(self, distance: Distance):
        if self.trajectory_data:
            points = filter(lambda p: self._trajectory_by_distance_filter(p, distance), self.trajectory_data)
            points_li = list(points)
            if points_li:
                return points_li[0]
        return None

    def get_cd_ad_distance(self, distance: Distance):
        point: TrajectoryData = self.get_trajectory_data_at_distance(distance)
        if point:
            mach = point.velocity().get_in(VelocityMPS) / self.sound_speed().get_in(VelocityMPS)
            return mach

    def get_drop_at_distances(self, distances: list):
        from datetime import datetime
        dt = datetime.now()
        ret = []
        step = self.profile.distance_step()
        step_value = step.value(step.units()) / 2
        drop_accuracy = 1

        for p in self.trajectory_data:
            td = p.travelled_distance().get_in(DistanceMeter)
            for d in distances:
                if math.fabs(td - d) < step_value:
                    drop = p.drop().get_in(DistanceCentimeter)
                    rounded_drop = round(drop, drop_accuracy)
                    ret.append((int(td), rounded_drop))

        return ret

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
