#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
