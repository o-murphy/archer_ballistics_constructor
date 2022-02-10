from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import aliased

try:
    from .models import *
    from .base import engine
except ImportError:
    from dbworker.models import *
    from dbworker.base import engine

SessMake = sessionmaker(bind=engine)

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    # data = [
    #     [98, "ELD Match", "Hornady", 3, 0.224, 5, 52, 0.247, 0.8],
    #     [115, "ELD Match", "Hornady", 3, 0.224, 5, 73, 0.398, 1.05],
    #     [118, "ELD Match", "Hornady", 3, 0.224, 5, 75, 0.467, 1.12],
    #     [120, "ELD Match", "Hornady", 3, 0.224, 5, 80, 0.485, 1.155],
    #     [280, "ELD-X", "Hornady", 3, 0.243, 7, 103, 0.512, 1.261],
    #     [282, "ELD Match", "Hornady", 3, 0.243, 7, 108, 0.536, 1.273],
    #     [438, "ELD Match", "Hornady", 3, 0.264, 9, 123, 0.506, 1.24],
    #     [442, "ELD Match", "Hornady", 3, 0.264, 9, 130, 0.554, 1.311],
    #     [444, "ELD Match", "Hornady", 3, 0.264, 9, 140, 0.646, 1.374],
    #     [449, "ELD-X", "Hornady", 3, 0.264, 9, 143, 0.625, 1.44],
    #     [450, "ELD Match", "Hornady", 3, 0.264, 9, 147, 0.697, 1.43],
    #     [574, "ELD-X", "Hornady", 3, 0.277, 11, 145, 0.536, 1.35],
    #     [682, "ELD-X", "Hornady", 3, 0.284, 12, 150, 0.574, 1.37],
    #     [687, "ELD Match", "Hornady", 3, 0.284, 12, 162, 0.67, 1.424],
    #     [688, "ELD-X", "Hornady", 3, 0.284, 12, 162, 0.613, 1.478],
    #     [693, "ELD-X", "Hornady", 3, 0.284, 12, 175, 0.66, 1.567],
    #     [696, "ELD Match", "Hornady", 3, 0.284, 12, 180, 0.796, 1.553],
    #     [910, "ELD Match", "Hornady", 3, 0.308, 14, 168, 0.523, 1.273],
    #     [914, "ELD-X", "Hornady", 3, 0.308, 14, 178, 0.535, 1.42],
    #     [915, "ELD Match", "Hornady", 3, 0.308, 14, 178, 0.547, 1.322],
    #     [928, "ELD-X", "Hornady", 3, 0.308, 14, 200, 0.597, 1.53],
    #     [929, "ELD Match", "Hornady", 3, 0.308, 14, 208, 0.67, 1.535],
    #     [931, "ELD-X", "Hornady", 3, 0.308, 14, 212, 0.673, 1.6],
    #     [932, "ELD-X", "Hornady", 3, 0.308, 14, 220, 0.65, 1.63],
    #     [1253, "ELD Match", "Hornady", 3, 0.338, 24, 285, 0.829, 1.743]
    # ]

    names = ["FMJ", "FMJ", "TSX", "TTSX", "TSX", "TSX", "TTSX", "TSX", "TAC X", "TSX", "TTSX", "TAC X", "TSX", "TAC X",
             "Match Burner", "Match Burner", "LRX", "Match Burner", "FB Varmint (22309)", "FULLBORE Target", "A-MAX",
             "BTHP Match", "HP Match", "V-MAX", "E-Tip", "V-MAX", "FMJ-BT", "V-MAX w/c", "SP W/C (#2266)", "SP (#2265)",
             "SP SX (#2240)", "HP", "SP", "V-MAX", "FMJ (22760B)", "BTHP Match", "SP (E539)", "Scenar (GB544)",
             "FB Tipped Varmageddon", "FBHP", "FB Tipped Varmageddon", "FB Tipped Varmageddon", "FBHP",
             "FB Tipped Varmageddon", "FBHP  Varmageddon", "Ballistic Tip Varmint", "Ballistic Tip Varmint",
             "Custom Competition", "E-Tip", "Ballistic Tip Varmint", "Ballistic Tip Varmint", "Bonded PERFORMANCE",
             "Custom Competition", "RDF", "Accubond", "Custom Competition", "Custom Competition", "HPBT MK", "HP MK",
             "FMJBT", "SBT", "SPT", "HPBT", "Tipped MatchKing (TMK)", "Tipped MatchKing (TMK)", "HPBT MK",
             "Tipped MatchKing (TMK)", "HPBT MatchKing", "HPBT MatchKing", "HPBT MatchKing", "HPBT MatchKing", "FMJ BT",
             "Spitz", "Spitz w/c", "TNT HP", "FMJ BT", "Gold Dot", "Gold Dot", "Gold Dot", "Varmint Soft Point (1053)",
             "Scirocco", "Scirocco", "Spartan HPBT", "Range master BTSP", "44gr VLR-4", "46gr VLR-5", "46gr VRG-2",
             "49gr VRG-3", "51gr VLR-4", "53gr VLR-5", "54gr Rangemaster", "58gr VRG-2", "55gr VRG-3", "58gr VLR-4",
             "60gr VLR-5", "65gr Rangemaster", "67gr VLR-4", "69gr VLR-5", "73gr VRG-2", "70gr VRG-3",
             "75gr Rangemaster", "5,6 mm MJG 5608", "AERO SB", "AERO SB", "AERO SB", "AERO SB", "AERO SOLR", "AERO SB",
             "AERO SOLR", "AERO SB", "Classic Hunter", "Classic Hunter", "Classic Hunter", "224EXBT/50-TIB",
             "223EXBT/54-TIB", "TRD T9013", "TRD T9014", "TRD T9015", "PST7", "PST7", "PST7", "BS", "PS", "BS", "PST7",
             "PST7FB", "PST7", "BS", "PST7FB", "PST7"]

    vendor = ["Barnaul (Russia)", "Barnaul (Russia)", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Barnes", "Berger", "Berger", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Hornady", "Lapua", "Lapua", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Nosler", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Sierra", "Speer", "Speer", "Speer", "Speer", "Speer", "Speer", "Speer", "Speer", "Speer", "Swift", "Swift", "Frontier", "Frontier", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Peregrine", "Lutz Möller", "Styria Arms", "Styria Arms", "Styria Arms", "Styria Arms", "Styria Arms", "Styria Arms", "Styria Arms", "Styria Arms", "Fox", "Fox", "Fox", "Titan", "Titan", "Ibex", "Ibex", "Ibex", "Viper", "Viper", "Viper", "Viper", "Viper", "Viper", "Viper", "Viper", "Viper", "Viper", "Viper", "Viper"]
    diameter = 0.224
    w = [55, 62, 45, 50, 50, 53, 55, 55, 55, 62, 62, 62, 70, 70, 52, 69, 77, 85, 52, 80.5, 52, 52, 53, 53, 55, 55, 55, 55, 55, 55, 55, 60, 60, 60, 62, 62, 55, 69, 35, 40, 40, 53, 55, 55, 62, 40, 50, 52, 55, 55, 60, 64, 69, 70, 70, 77, 80, 52, 53, 55, 55, 55, 55, 60, 69, 69, 77, 77, 80, 90, 95, 55, 55, 55, 55, 62, 55, 62, 75, 70, 62, 75, 52, 45, 44, 46, 46, 49, 51, 53, 54, 58, 55, 58, 60, 65, 67, 69, 73, 70, 75, 44, 35, 40, 45, 50, 50, 51, 58, 60, 45, 50, 55, 50, 54, 35, 45, 50, 30, 40, 45, 45, 47, 50, 50, 50, 55, 55, 55, 60]
    bc = [0.255, 0.248, 0.188, 0.229, 0.197, 0.204, 0.272, 0.209, 0.209, 0.287, 0.294, 0.287, 0.314, 0.314, 0.224, 0.339, 0.404, 0.41, 0.201, 0.441, 0.247, 0.229, 0.218, 0.29, 0.305, 0.252, 0.243, 0.235, 0.235, 0.235, 0.214, 0.271, 0.264, 0.256, 0.274, 0.27, 0.185, 0.341, 0.12, 0.158, 0.211, 0.303, 0.21, 0.255, 0.251, 0.221, 0.238, 0.22, 0.305, 0.267, 0.27, 0.231, 0.305, 0.416, 0.37, 0.34, 0.415, 0.225, 0.214, 0.272, 0.25, 0.237, 0.185, 0.323, 0.375, 0.301, 0.42, 0.372, 0.461, 0.563, 0.6, 0.269, 0.212, 0.212, 0.233, 0.307, 0.25, 0.31, 0.411, 0.214, 0.307, 0.419, 0.23, 0.217, 0.198, 0.198, 0.122, 0.122, 0.248, 0.248, 0.291, 0.1434, 0.146, 0.281, 0.281, 0.4, 0.321, 0.321, 0.161, 0.161, 0.554, 0.244, 0.1179, 0.167, 0.1768, 0.177, 0.265, 0.1867, 0.3045, 0.2554, 0.163, 0.175, 0.185, 0.289, 0.31, 0.136, 0.171, 0.207, 0.122, 0.085, 0.112, 0.092, 0.169, 0.138, 0.17, 0.117, 0.2, 0.152, 0.212, 0.286]
    ln = [0.787, 0.838, 0.698, 0.812, 0.736, 0.796, 0.898, 0.797, 0.797, 0.942, 0.973, 0.942, 1.036, 1.036, 0.705, 0.915, 1.182, 1.068, 0.72, 1.091, 0.8, 0.713, 0.715, 0.827, 0.9, 0.811, 0.735, 0.811, 0.715, 0.715, 0.697, 0.804, 0.75, 0.87, 0.82, 0.82, 0.675, 0.935, 0.52, 0.565, 0.665, 0.83, 0.7, 0.795, 0.77, 0.705, 0.8, 0.717, 0.9, 0.81, 0.851, 0.8, 0.902, 0.965, 0.965, 0.973, 1.078, 0.698, 0.701, 0.752, 0.724, 0.715, 0.715, 0.897, 0.982, 0.9, 1.066, 0.994, 1.066, 1.171, 1.2986, 0.743, 0.743, 0.743, 0.743, 0.8, 0.743, 0.85, 1.085, 0.79, 0.928, 1.085, 0.78, 0.736, 0.713, 0.713, 0.636, 0.636, 0.833, 0.833, 0.909, 0.746, 0.746, 0.913, 0.913, 1.072, 1.02, 1.02, 0.921, 0.921, 1.203, 0.728, 0.575, 0.638, 0.728, 0.764, 0.868, 0.811, 0.945, 0.949, 0.748, 0.807, 0.87, 0.887, 0.877, 0.571, 0.689, 0.768, 0.482, 0.57, 0.638, 0.62, 0.669, 0.696, 0.79, 0.74, 1.31, 0.697, 0.852, 0.886]


    sess: Session = SessMake()

    # for i in [0.224, 0.243, 0.264, 0.277, 0.284, 0.308, 0.338]:
    #     if not sess.query(Diameter).filter_by(diameter=i).first():
    #         diameter = sess.add(Diameter(i))
    # sess.commit()

    for i in range(len(names)):
        if not sess.query(Bullet).filter_by(name=vendor[i] + ' ' + names[i]).first():

            bullet = Bullet(
                name=vendor[i] + ' ' + names[i],
                weight=w[i],
                length=ln[i],
                diameter_id=sess.query(Diameter).filter_by(diameter=diameter).first().id
            )
            sess.add(bullet)
            sess.commit()

            sess.add(DragFunc('G1', bc[i], 'default bc', bullet.id))
    sess.commit()
