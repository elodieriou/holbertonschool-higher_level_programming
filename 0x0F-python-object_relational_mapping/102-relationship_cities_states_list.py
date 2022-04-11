#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""

if __name__ == "__main__":
    from sys import argv
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()
    for instance_city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(instance_city.id, instance_city.name, instance_city.state.name))
    session.close()
