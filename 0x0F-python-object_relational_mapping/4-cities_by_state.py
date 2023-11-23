#!/usr/bin/python3
"""
A PyScript that displays values from cities table from hbtn_0e_4_usa db
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Filter query code for the database SQLinjection-proof"""

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database> \
               <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)

        crs = db.cursor()
        crs.execute("SELECT cities.id, cities.name, states.name \
                     FROM cities INNER JOIN states ON \
                     states.id=cities.state_id ORDER BY id ASC")

        itemrows = crs.fetchall()
        for item in itemrows:
            print(item)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    finally:
        crs.close()
        db.close()
