#!/usr/bin/python3
"""
A PyScript that displays values from states table from hbtn_0e_0_usa
db where name matched the argument passed avoiding SQL injections
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Filter query code for the database SQLinjection-proof"""

    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> \
               <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)

        crs = db.cursor()
        crs.execute("SELECT * FROM states WHERE name LIKE \
                     %s ORDER BY id ASC", (state_name, ))

        itemrows = crs.fetchall()
        for item in itemrows:
            print(item)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    finally:
        crs.close()
        db.close()
