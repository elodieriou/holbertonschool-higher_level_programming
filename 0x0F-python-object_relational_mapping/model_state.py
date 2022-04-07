#!/usr/bin/python3
"""This module contains the class definition of a State and an instance
 Base = declarative_base()"""
from sys import argv
import MySQLdb
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
Base = declarative_base()


class State(Base):
    """The class States"""
    __tablename__ = 'states'
    id = Column(Integer,  nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
