#!/usr/bin/python3
"""Using SQLAlchemy ORM"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Class inherits from base class

    Attributes (sql columns):
        __tablename__: sql table name
        id: state id
        name: state name
    """

    __tablename__ = 'states'
    id = Column(
        'id',
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column('name', String(128), nullable=False)
