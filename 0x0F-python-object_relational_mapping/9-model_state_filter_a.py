#!/usr/bin/python3
"""Contains a"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv as a
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    cn = f'mysql+mysqldb://{a[1]}:{a[2]}@localhost:3306/{a[3]}'
    sqlEngine = create_engine(cn, pool_pre_ping=True)
    Session = sessionmaker(bind=sqlEngine)
    sesn = Session()
    qry = sesn.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for eachState in qry:
        print(f'{eachState.id}: {eachState.name}')

    sesn.close()
