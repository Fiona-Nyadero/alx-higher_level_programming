#!/usr/bin/python3
"""
A PyScript that displays values from states table from
hbtn_0e_0_usa db where name matched the argument passed
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Filter query code for the database """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    crs = db.cursor()
    crs.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                 ORDER BY id ASC".format(sys.argv[4]))
    itemrows = crs.fetchall()
    for item in itemrows:
        print(item)
    crs.close()
    db.close()
