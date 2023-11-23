#!/usr/bin/python3
"""
A Python Script that lists all states
starting with 'N' from hbtn_0e_0_usa db
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Filter query code for the database """
    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    itemrows = crs.fetchall()
    for item in itemrows:
        print(item)
    crs.close()
    db.close()
