#!/usr/bin/python3
"""Filter states"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    dbConnection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    selQuery = 'SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY id'
    cursorDb = dbConnection.cursor()
    cursorDb.execute(selQuery)
    for row in cursorDb.fetchall():
        print(row)
    cursorDb.close()
    dbConnection.close()
