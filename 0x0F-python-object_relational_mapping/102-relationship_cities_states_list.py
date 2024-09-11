#!/usr/bin/python3
"""From city"""
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
    sqlData = sesn.query(State).join(City).order_by(City.id).all()
    for st in sqlData:
        for cty in st.cities:
            print(f'{cty.id}: {cty.name} -> {st.name}')
    sesn.close()
