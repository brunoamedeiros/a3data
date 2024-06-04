""" Base class for all models
"""


from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from app.infra.config import settings


class Base(DeclarativeBase):
    """ Base class for all models
    """


engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI))
