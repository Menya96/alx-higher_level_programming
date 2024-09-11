#!/usr/bin/python3
"""List relationship"""
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
    data = sesn.query(State).outerjoin(City).order_by(State.id, City.id).all()
    for st in data:
        print(f'{st.id}: {st.name}')
        for cty in st.cities:
            print(f'\t{cty.id}: {cty.name}')
    sesn.close()
