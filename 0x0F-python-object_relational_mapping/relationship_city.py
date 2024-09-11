#!/usr/bin/python3
"""SQL table City class module"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Class inherits from base class

    Attributes (sql columns):
        __tablename__: sql table name
        id: city id
        name: city name
        state_id: city's state id (foreign key)
    """

    __tablename__ = 'cities'
    id = Column(
        'id',
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column('name', String(128), nullable=False)
    state_id = Column(
        'state_id',
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
