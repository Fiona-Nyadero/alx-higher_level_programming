#!/usr/bin/python3
""" A PyScript that lists all states from hbtn_0e_0_usa db """

import MySQLdb
import sys

if __name__ == "__main__":
    """ Listing query code for the database """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    crs = db.cursor()
    crs.execute("SELECT * FROM states")
    itemrows = crs.fetchall()
    for item in itemrows:
        print(item)
    crs.close()
    db.close()
