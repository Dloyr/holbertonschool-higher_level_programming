#!/usr/bin/python3

"""Same as taks 2 but using safe filter"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    database = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306)

    cursor = database.cursor()

    query = "SELECT * FROM states \
        WHERE name LIKE name = %s ORDER BY id ASC"

    cursor.execute(query, (state_name_searched,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    database.close()
