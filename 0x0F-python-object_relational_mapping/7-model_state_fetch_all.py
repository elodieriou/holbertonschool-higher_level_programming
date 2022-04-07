#!/usr/bin/python3
"""Script that lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
for instance in session.query(State).order_by(State.id):
    print("{}: {}".format(instance.id, instance.name))
session.close()

if __name__ == "__main__":
    argv
    Base, State
    create_engine
    sessionmaker
