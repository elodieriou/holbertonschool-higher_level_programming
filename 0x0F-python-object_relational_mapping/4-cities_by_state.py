#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
cursor = connection.cursor()
cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")
query_rows = cursor.fetchall()
for row in query_rows:
    print(row)
cursor.close()
connection.close()

if __name__ == "__main__":
    MySQLdb
    argv
