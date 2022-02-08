from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import aliased

try:
    from .models import *
    from .base import engine
except ImportError:
    from dbworker.models import *
    from dbworker.base import engine

SessMake = sessionmaker(bind=engine)

temp_data = {
    "rifleName": "G7 template",
    "caliberName": ".224 Remington",
    "sh": 90,
    "twist": 10,
    "caliberShort": ".224",
    "rightTwist": True,

    "bulletName": "",
    "weight": 175.0,
    "length": 0.9,
    "diameter": 0.224,
    "dragType": 1,
    "dfdata": None,
    
    "weightTile": "175gr",
    "multiBC": 0,
    "bc": 0.169,
    "bcTable": [
        [
            914,
            0
        ],
        [
            762,
            0
        ],
        [
            609,
            0
        ],
        [
            457,
            0
        ],
        [
            0,
            0
        ]
    ],
    "cartridgeName": "",
    "mv": 800,
    "temp": 15,
    "ts": 1.55,
    "z_pressure": 750,
    "z_angle": 0,
    "z_humidity": 50,
    "z_temp": 15,
    "z_azimuth": 270,
    "z_powder_temp": 15,
    "z_latitude": 0,
    "z_x": 0,
    "z_y": 0,
    "z_d": 100,
    "": 0.246
}


def get_rifles():
    session = SessMake(bind=engine)
    rifles = session.query(Rifle).all()
    return rifles


def get_rifle(id):
    session = SessMake(bind=engine)
    rifle = session.query(Rifle).get(id)
    return rifle


def delete_rifle(id):
    session: Session = SessMake(bind=engine)
    rifle = session.query(Rifle).get(id)
    session.delete(rifle)
    session.commit()


def update_rifle(id, data):
    session: Session = SessMake(bind=engine)
    rifle = session.query(Rifle).get(id)
    for k, v in data.items():
        if hasattr(rifle, k):
            setattr(rifle, k, v)
    session.commit()


def get_cartridges():
    session = SessMake(bind=engine)
    cartridges = session.query(Cartridge).all()
    return cartridges


def get_cartridge(id):
    session = SessMake(bind=engine)
    cartridge = session.query(Cartridge).get(id)
    return cartridge


def delete_cartridge(id):
    session: Session = SessMake(bind=engine)
    cartridge = session.query(Cartridge).get(id)
    session.delete(cartridge)
    session.commit()


def update_cartridge(id, data):
    session: Session = SessMake(bind=engine)
    cartridge = session.query(Cartridge).get(id)
    for k, v in data.items():
        if hasattr(cartridge, k):
            setattr(cartridge, k, v)
    session.commit()


def get_bullets():
    session = SessMake(bind=engine)
    bullets = session.query(Bullet).all()
    return bullets


def get_bullet(id):
    session = SessMake(bind=engine)
    bullet = session.query(Bullet).get(id)
    return bullet


def delete_bullet(id):
    session: Session = SessMake(bind=engine)
    bullet = session.query(Bullet).get(id)
    session.delete(bullet)
    session.commit()


def update_bullet(id, data):
    session: Session = SessMake(bind=engine)
    bullet = session.query(Bullet).get(id)
    for k, v in data.items():
        if hasattr(bullet, k):
            setattr(bullet, k, v)
    session.commit()


def add_rifle(rifleName, sh, twist, rightTwist, caliberName, diameter, **kwargs):
    session: Session = SessMake(bind=engine)

    caliber = session.query(Caliber).filter_by(name=caliberName).first()

    if not caliber and d:
        caliber = Caliber(caliberName, d.id)
        session.add(caliber)

    if caliber:
        rifle = Rifle(rifleName, caliber.id, sh, twist, rightTwist)
        session.add(rifle)

    session.commit()
    session.close()


def merge_caliber(name):
    session: Session = SessMake(bind=engine)
    caliber = session.query(Caliber).filter_by(name=name).first()
    # if not caliber:
    #     caliber = Caliber(name, diameter_id)
    #     session.add(caliber)
    #     session.commit()
    return caliber


def merge_cartridge(name, caliber, mv, temp, ts, id=None):
    session: Session = SessMake(bind=engine)

    c = merge_caliber(caliber)

    if c:
        cartridge = session.query(Cartridge).get(id)
        if cartridge:
            cartridge.name = name
            cartridge.caliber_id = c.id
            cartridge.mv = mv
            cartridge.temp = temp
            cartridge.ts = ts
        else:
            cartridge = Cartridge(name, mv, temp, ts, caliber.id)
            session.add(cartridge)
        session.commit()
        return cartridge


def merge_bullet(name, weight, length, diameter, bc, id=None):
    session: Session = SessMake(bind=engine)

    d = merge_diameter(diameter)
    if d:
        g1 = bc['G1'] if 'G1' in bc else None
        g7 = bc['G7'] if 'G7' in bc else None
        bullet = session.query(Bullet).get(id)
        if bullet:
            bullet.name = name
            bullet.weight = weight
            bullet.length = length
            bullet.diameter_id = d.id
            bullet.g1 = g1
            bullet.g7 = g7
        else:
            bullet = Bullet(name, weight, length, d.id, g1, g7)
            session.add(bullet)

        session.commit()

        if 'Custom' in bc:
            merge_drag_func(bullet.id, bc['Custom'])

        if 'MultiBC' in bc:
            merge_multi_bc(bullet.id, *bc['MultiBC'])
        return bullet


def merge_diameter(diameter):
    session: Session = SessMake(bind=engine)

    d = session.query(Diameter).filter_by(diameter=diameter).first()

    if not d:
        d = Diameter(diameter=diameter)
        session.add(d)
        session.commit()
    return d


def merge_multi_bc(id, *args):
    session: Session = SessMake(bind=engine)
    mbc = session.query(MultiBC).filter_by(bullet_id=id).first()
    if mbc:
        cols = [k for k in MultiBC.__dict__.keys() if k.startswith('v') or k.startswith('bc')]
        for i, k in enumerate(cols):
            setattr(mbc, k, args[i])
    else:
        session.add(MultiBC(id, *args))
    session.commit()
    return mbc


def merge_drag_func(id, data):
    session: Session = SessMake(bind=engine)
    drag_func = session.query(DragFunc).filter_by(bullet_id=id).first()
    if not drag_func:
        session.add(DragFunc(id, data))
    else:
        drag_func.data = data
    session.commit()
    return drag_func


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    merge_bullet('bull1', 175, 0.9, .30,
                   {'G1': .169,
                    "Custom": [[1, 1], [0, 0]],
                    "MultiBC": [.1, .1, .1, 0, 0, 700, 800, 900, 0, 0]
                    }, id=1)
