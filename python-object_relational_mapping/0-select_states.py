#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to the database and fetches all states sorted by id.
    """
    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
