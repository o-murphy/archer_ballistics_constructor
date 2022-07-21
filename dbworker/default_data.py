from dbworker import db
from dbworker.models import *


def get_defaults():
    try:
        sess = db.SessMake()
        rifle: Rifle = sess.query(Rifle).get(0)
        cart: Cartridge = sess.query(Cartridge).filter_by(caliber_id=rifle.caliber_id, attrs='r').first()
        bullet = sess.query(Bullet).get(cart.bullet_id)
        drags = sess.query(DragFunc).filter_by(bullet_id=bullet.id).all()

        data = {
            'rifleName': rifle.name,
            'caliberName': rifle.caliber.name,
            'sh': rifle.sh,
            'twist': rifle.twist,
            'caliberShort': '',
            'rightTwist': rifle.is_right,
            'mv': cart.mv,
            'cartridgeName': cart.name,
            'temp': cart.temp,
            'ts': cart.ts,
            'bulletName': bullet.name,
            'weight': bullet.weight,
            'length': bullet.length,
            'diameter': bullet.diameter.diameter,
            'drags': drags,
            'drag_idx': 0,
            'z_d': 100,
            'z_x': 0,
            'z_y': 0,
            'z_pressure': 760,
            "z_angle": 0,
            "z_temp": 15,
            "z_humidity": 50,
            "z_azimuth": 270,
            "z_latitude": 0,
            "z_powder_temp": 15,
        }

        return data
    except Exception as err:
        return


def get_templates(rif_id, catr_id):
    try:
        sess = db.SessMake()
        rifle: Rifle = sess.query(Rifle).get(rif_id)
        cart: Cartridge = sess.query(Cartridge).get(catr_id)
        bullet = sess.query(Bullet).get(cart.bullet_id)
        drags = sess.query(DragFunc).filter_by(bullet_id=bullet.id).all()

        data = {
            'rifleName': rifle.name,
            'caliberName': rifle.caliber.name,
            'sh': rifle.sh,
            'twist': rifle.twist,
            'caliberShort': '',
            'rightTwist': rifle.is_right,
            'mv': cart.mv,
            'cartridgeName': cart.name,
            'temp': cart.temp,
            'ts': cart.ts,
            'bulletName': bullet.name,
            'weight': bullet.weight,
            'length': bullet.length,
            'diameter': bullet.diameter.diameter,
            'drags': drags,
            'drag_idx': 0
        }

        return data
    except Exception as err:
        return
