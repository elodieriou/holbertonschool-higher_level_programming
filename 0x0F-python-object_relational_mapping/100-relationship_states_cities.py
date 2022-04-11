#!/usr/bin/python3
"""script that creates the State “California” with the City
 “San Francisco” from the database hbtn_0e_100_usa"""

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
    create_state = State(name="California")
    create_state.cities.append(City(name="San Francisco"))

    session.add(create_state)
    session.commit()
    session.close()
