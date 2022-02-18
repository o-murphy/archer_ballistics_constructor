from dbworker import db
from dbworker.models import *


def get_defaults():
    try:
        sess = db.SessMake()
        # rifle: Rifle = sess.query(Rifle).filter_by(attrs='r').first()
        rifle: Rifle = sess.query(Rifle).get(0)
        cart: Cartridge = sess.query(Cartridge).filter_by(caliber_id=rifle.caliber_id, attrs='r').first()
        bullet = sess.query(Bullet).get(cart.bullet_id)
        drags = sess.query(DragFunc).filter_by(bullet_id=bullet.id).all()
        print(rifle.__dict__)
        print(cart.__dict__)
        print(bullet.__dict__)
        print([d.__dict__ for d in drags])

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
