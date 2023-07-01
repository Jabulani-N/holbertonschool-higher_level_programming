#!/usr/bin/python3
"""moldue with a script that lists
all states with a name starting with N from the database hbtn_0e_0_usa

does not activate when imported

script should take 3 arguments:
mysql username, mysql password and database name(no argument validation needed)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""

import MySQLdb
import sys


def filter_states():
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute(
                "SELECT id, name FROM states WHERE\
                 BINARY name \
                 LIKE \"N%\" ORDER BY id;"
               )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()


if __name__ == '__main__':
    filter_states()
