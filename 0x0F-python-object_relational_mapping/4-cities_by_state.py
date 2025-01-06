#!/usr/bin/python3
"""
Script that lists all cities from database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
     def list_cities():
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute(
            """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            """
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()

    if sys.argv[0].endswith("0-select_states.py"):
        list_states()
    elif sys.argv[0].endswith("1-filter_states.py"):
        filter_states()
    elif sys.argv[0].endswith("2-my_filter_states.py"):
        my_filter_states()
    elif sys.argv[0].endswith("3-my_safe_filter_states.py"):
        my_safe_filter_states()
    elif sys.argv[0].endswith("4-cities_by_state.py"):
        list_cities()
