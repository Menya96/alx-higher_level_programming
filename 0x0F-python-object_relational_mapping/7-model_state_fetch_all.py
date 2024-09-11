#!/usr/bin/python3
"""Listing all states through SQLAlchemy ORM"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv as a
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    cn = f'mysql+mysqldb://{a[1]}:{a[2]}@localhost:3306/{a[3]}'
    sqlEngine = create_engine(cn, pool_pre_ping=True)
    Session = sessionmaker(bind=sqlEngine)
    sesn = Session()

    for eachState in sesn.query(State).order_by(State.id):
        print(f'{eachState.id}: {eachState.name}')

    sesn.close()
