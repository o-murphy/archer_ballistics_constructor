from bin.archer_ballistics import archer_ballistics


archer_ballistics.set_profile(
    {
        "SightHeight": 90,
        "Zero": 100,
        "H_zero": 0,
        "V_zero": 0,
        "twist_value": 11,
        "is_right": True,
        "Twist": 11,
        "V0": 800,
        "T0": 15,
        "PowderSens": 1.55,
        "DragFunc": 7,
        "BalCoef": [
            0.275,
            0.0,
            0.0,
            0.0,
            0.0
        ],
        "BVelocity": [
            800,
            -1,
            -1,
            -1,
            -1
        ],
        "Diameter": 0.308,
        "Length": 1.3,
        "Weight": 150.0,
        "Temperature": 15,
        "P_Temperature": 15,
        "Humidity": 50,
        "Pressure": 760,
        "Angle": 0,
        "Azimuth": 270,
        "Latitude": 0
    }
)

archer_ballistics.set_drag_function()

ret_data = archer_ballistics.get_drag_function()
print(ret_data)
