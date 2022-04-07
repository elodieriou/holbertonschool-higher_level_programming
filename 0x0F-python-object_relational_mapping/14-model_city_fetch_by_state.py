#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
all_city = session.query(State, City).join(State).all()
for state, city in all_city:
    print("{}: ({}) {}".format(state.name, city.id, city.name))
session.close()

if __name__ == "__main__":
    argv
    Base, State
    create_engine
    sessionmaker
    City
