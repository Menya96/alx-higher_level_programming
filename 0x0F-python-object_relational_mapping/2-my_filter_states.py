#!/usr/bin/python3
"""Filter states by user input"""
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
    query = 'SELECT * FROM states WHERE BINARY name="{}" ORDER \
        BY id'.format(argv[4])
    cursorDb = dbConnection.cursor()
    cursorDb.execute(query)
    for row in cursorDb.fetchall():
        print(row)
    cursorDb.close()
    dbConnection.close()
