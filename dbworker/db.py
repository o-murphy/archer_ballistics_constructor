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
