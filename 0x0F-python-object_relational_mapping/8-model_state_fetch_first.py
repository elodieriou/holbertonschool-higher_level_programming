#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa"""
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
try:
    first_state = session.query(State).first()
    print("{}: {}".format(first_state.id, first_state.name))
except Exception:
    print("Nothing")
session.close()

if __name__ == "__main__":
    argv
    Base, State
    create_engine
    sessionmaker
