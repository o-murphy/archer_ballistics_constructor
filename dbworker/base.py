from sqlalchemy import create_engine
from .models import *


# engine = create_engine('sqlite:///:memory:', echo=False)
engine = create_engine('sqlite:///db.db', echo=False)


# Base.metadata.create_all(engine)

