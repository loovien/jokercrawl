# -*- coding: utf-8 -*-


import MySQLdb
import datetime
from MySQLdb.cursors import DictCursor


def time_parse():
    now = datetime.datetime.now()
    str_time = now.strftime("%m-%d %H:%M")
    print(">>>>> parse time:")
    with_year = "{year}-{suffix}".format(year="2017", suffix=str_time)
    print(with_year)
    new_time = datetime.datetime.strptime(with_year, "%Y-%m-%d %H:%M")
    print(">>>>> string to time:")
    print(new_time.timestamp())


def fetch_mysql():
    conn = MySQLdb.Connect(host="localhost", user="root", password="111111", db="hahajok", port=3306,
                           charset="utf8", cursorclass=DictCursor)
    cursor = conn.cursor()
    cursor.execute("select * from user")
    result_set = cursor.fetchall()
    print(list(result_set))
    cursor.close()


if __name__ == '__main__':
    #time_parse()
    fetch_mysql()
