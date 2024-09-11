#!/usr/bin/python3
"""City relationship"""
from relationship_state import Base, State
from sqlalchemy import create_engine
from sys import argv as a
from sqlalchemy.orm import sessionmaker
from relationship_city import City


if __name__ == '__main__':
    cnctor = f'mysql+mysqldb://{a[1]}:{a[2]}@localhost:3306/{a[3]}'
    sqlEngine = create_engine(cnctor, pool_pre_ping=True)
    Base.metadata.create_all(sqlEngine)
    Session = sessionmaker(bind=sqlEngine)
    sesn = Session()
    calif = State(name='California')
    sanFran = City(name='San Francisco')
    calif.cities.append(sanFran)
    sesn.add(calif)
    sesn.commit()
    sesn.close()
