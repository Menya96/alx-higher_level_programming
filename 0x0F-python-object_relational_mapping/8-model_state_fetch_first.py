#!/usr/bin/python3
"""First state"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv as a
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    cn = f'mysql+mysqldb://{a[1]}:{a[2]}@localhost:3306/{a[3]}'
    sqlEngine = create_engine(cn, pool_pre_ping=True)
    Session = sessionmaker(bind=sqlEngine)
    sesn = Session()
    result = sesn.query(State).order_by(State.id).first()
    if not result:
        print('Nothing')
    else:
        print(f'{result.id}: {result.name}')

    sesn.close()
