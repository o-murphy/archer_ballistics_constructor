from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


#     def __repr__(self):
#         return self.name
#
#     def __str__(self):
#         return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


class Diameter(Base):
    __tablename__ = 'diameter'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    diameter = Column(Integer, unique=True)

    caliber = relationship('Caliber', back_populates='diameter')
    bullet = relationship('Bullet', back_populates='diameter')

    def __init__(self, diameter):
        self.diameter = diameter


class Caliber(Base):
    __tablename__ = 'caliber'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String, unique=True)

    diameter_id = Column(Integer, ForeignKey('diameter.id'))
    diameter = relationship('Diameter', back_populates='caliber')

    rifle = relationship("Rifle", back_populates="caliber")
    cartridge = relationship("Cartridge", back_populates="caliber")

    def __init__(self, name, diameter_id):
        self.name = name
        self.diameter_id = diameter_id


class Rifle(Base):
    __tablename__ = 'rifle'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    sh = Column(Integer)
    twist = Column(Integer)
    is_right = Column(Boolean)
    tile = Column(String)
    attrs = Column(String)

    caliber_id = Column(Integer, ForeignKey('caliber.id'))
    caliber = relationship("Caliber", back_populates="rifle")

    template = relationship("Template", back_populates="rifle")

    def __init__(self, name, caliber_id, sh, twist, is_right, tile, attrs='r'):
        self.name = name
        self.caliber_id = caliber_id
        self.sh = sh
        self.twist = twist
        self.is_right = is_right
        self.tile = tile
        self.attrs = attrs


class Cartridge(Base):
    __tablename__ = 'cartridge'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    mv = Column(Integer)
    temp = Column(Integer)
    ts = Column(Integer)
    attrs = Column(String)

    caliber_id = Column(Integer, ForeignKey('caliber.id'))
    caliber = relationship("Caliber", back_populates="cartridge")

    bullet_id = Column(Integer, ForeignKey('bullet.id'))
    bullet = relationship("Bullet", back_populates="cartridge")

    template = relationship("Template", back_populates="cartridge")

    def __init__(self, name, mv, temp, ts, caliber_id, bullet_id, attrs='r'):
        self.name = name
        self.caliber_id = caliber_id
        self.ts = ts
        self.mv = mv
        self.temp = temp
        self.attrs = attrs
        self.bullet_id = bullet_id


class Bullet(Base):
    __tablename__ = 'bullet'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)
    weight = Column(Integer)
    length = Column(Integer)
    attrs = Column(String)

    diameter_id = Column(Integer, ForeignKey('diameter.id'))
    diameter = relationship('Diameter', back_populates='bullet')

    drag_func = relationship("DragFunc", back_populates="bullet")
    cartridge = relationship("Cartridge", back_populates="bullet")

    def __init__(self, name, weight, length, diameter_id, attrs='r'):
        self.name = name
        self.weight = weight
        self.length = length
        self.attrs = attrs
        self.diameter_id = diameter_id


class DragFunc(Base):
    __tablename__ = 'drag_func'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    bullet_id = Column(Integer, ForeignKey('bullet.id'))
    bullet = relationship('Bullet', back_populates='drag_func')
    drag_type = Column(String)
    data = Column(JSON)
    comment = Column(String)
    attrs = Column(String)

    template = relationship("Template", back_populates="drag_func")

    def __init__(self, drag_type, data, comment, bullet_id=None, attrs='r'):
        self.drag_type = drag_type
        self.data = data
        self.comment = comment
        self.attrs = attrs
        self.bullet_id = bullet_id


class Template(Base):
    __tablename__ = 'template'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String)

    rifle_id = Column(Integer, ForeignKey('rifle.id'))
    rifle = relationship('Rifle', back_populates='template')

    cartridge_id = Column(Integer, ForeignKey('cartridge.id'))
    cartridge = relationship('Cartridge', back_populates='template')

    drag_func_id = Column(Integer, ForeignKey('drag_func.id'))
    drag_func = relationship('DragFunc', back_populates='template')

    def __init__(self, name, rifle_id, cartridge_id, drag_func_id):
        self.name = name
        self.rifle_id = rifle_id
        self.cartridge_id = cartridge_id
        self.drag_func_id = drag_func_id
