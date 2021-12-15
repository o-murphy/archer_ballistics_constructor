from bin import archer_ballistics


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


if __name__ == '__main__':
    pass
