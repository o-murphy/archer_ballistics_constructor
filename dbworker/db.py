from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import aliased

from .models import *
from .base import engine

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
    rifles = session.query(Cartridge).all()
    return rifles


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


def add_rifle(rifleName, sh, twist, rightTwist, caliberName, diameter, **kwargs):
    session: Session = SessMake(bind=engine)
    d = session.query(Diameter).filter_by(diameter=diameter).first()

    if not d:
        d = Diameter(diameter=diameter)
        session.add(d)

    caliber = session.query(Caliber).filter_by(name=caliberName).first()

    if not caliber and d:
        caliber = Caliber(caliberName, d.id)
        session.add(caliber)

    if caliber:
        rifle = Rifle(rifleName, caliber.id, sh, twist, rightTwist)
        session.add(rifle)

    session.commit()
    session.close()


def add_cartridge(diameter, caliberName, cartridgeName, mv, temp, ts, **kwargs):
    session: Session = SessMake(bind=engine)

    d = session.query(Diameter).filter_by(diameter=diameter).first()

    if not d:
        d = Diameter(diameter=diameter)
        session.add(d)

    caliber = session.query(Caliber).filter_by(name=caliberName).first()

    if not caliber and d:
        caliber = Caliber(caliberName, d.id)
        session.add(caliber)

    if caliber:
        cartridge = Cartridge(cartridgeName, mv, temp, ts, caliber.id)
        session.add(cartridge)

    session.commit()
    session.close()


def add_bullet(bulletName, weight, length, diameter, dragType, dfdata, multiBC, bcTable, bc, mv, **kwargs):
    session: Session = SessMake(bind=engine)

    d = session.query(Diameter).filter_by(diameter=diameter).first()

    if not d:
        d = Diameter(diameter=diameter)
        session.add(d)

    if multiBC == 0:
        mbc = {
            'bc0': bc,
            'bc1': -1,
            'bc2': -1,
            'bc3': -1,
            'bc4': -1,
            'v0': mv,
            'v1': 0,
            'v2': 0,
            'v3': 0,
            'v4': 0
        }
    else:
        mbc = {}
        for i, (v, bc) in enumerate(bcTable):
            mbc[f'bc{i}'] = bc
            mbc[f'v{i}'] = v

    if d:
        bullet = Bullet(bulletName, weight, length, d.id, dragType, dfdata, **mbc)
        session.add(bullet)

    session.commit()
    session.close()


if __name__ == '__main__':
    add_rifle(**temp_data)
    add_cartridge(**temp_data)
    add_bullet(**temp_data)
