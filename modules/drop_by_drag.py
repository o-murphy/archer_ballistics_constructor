from archer_ballistics import archer_ballistics


def calculate(drag_function: list, distances: list) -> list:
    data = []
    for x, y in drag_function[::-1]:
        data.append(x)
        data.append(y)
    archer_ballistics.set_drag_function(data)
    return archer_ballistics.get_drop_at_distance(distances)


if __name__ == '__main__':
    print(archer_ballistics.get_drop_at_distance([100, 200]))
