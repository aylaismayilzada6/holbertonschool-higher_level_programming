#!/usr/bin/python3
"""
Safe filter states (SQL injection protected)
"""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
