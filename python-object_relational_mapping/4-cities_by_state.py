#!/usr/bin/python3
""" lists all cities from hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    database = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306)

    cursor = database.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC"
    cursor.execute(query)

    cities = cursor.fetchall()

    for citie in cities:
        print(citie)

    cursor.close()
    database.close()