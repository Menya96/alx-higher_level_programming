#!/usr/bin/python3
"""SQL table State class module"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


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
    cities = relationship('City', backref='state', cascade='all, delete')
