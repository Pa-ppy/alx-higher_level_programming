#!/usr/bin/python3
"""
Script that displays values in states table matching the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
     def my_filter_states():
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(sys.argv[4])
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
