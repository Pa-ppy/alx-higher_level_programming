#!/usr/bin/python3
"""
Script to select and list all states from the database
hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    def list_states():
        """
        Connects to the database and retrieves all states
        ordered by their ID in ascending order.
        """
        try:
            db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3])
            cur = db.cursor()
            cur.execute("SELECT * FROM states ORDER BY id ASC;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except MySQLdb.Error as e:
            print(f"Error: {e}")
        finally:
            cur.close()
            db.close()
