#!/usr/bin/python3
"""Get a state"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv as a
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    cn = f'mysql+mysqldb://{a[1]}:{a[2]}@localhost:3306/{a[3]}'
    sqlEngine = create_engine(cn, pool_pre_ping=True)
    Base.metadata.create_all(sqlEngine)
    Session = sessionmaker(bind=sqlEngine)
    sesn = Session()
    userQuery = sesn.query(State).filter(State.name == a[4]).first()
    if not userQuery:
        print('Not found')
    else:
        print(f'{userQuery.id}')

    sesn.close()
