#!/usr/bin/python3
"""This module contains the class definition of a City and an instance
 Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """The class City"""
    __tablename__ = 'cities'
    id = Column(Integer,  nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False, )
