#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument. But this time,
 write one that is safe from MySQL injections"""
import MySQLdb
from sys import argv

connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3], charset="utf8")
cursor = connection.cursor()
cursor.execute("SELECT * FROM states WHERE Name = %s ORDER BY id ASC",
               (argv[4],))
query_rows = cursor.fetchall()
for row in query_rows:
    print(row)
cursor.close()
connection.close()

if __name__ == "__main__":
    MySQLdb
    argv
