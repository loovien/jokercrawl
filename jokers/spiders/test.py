# -*- coding: utf-8 -*-


import MySQLdb
import datetime
import time
import random
from MySQLdb.cursors import DictCursor

def str_test():
    string = list("我是一个中国人")
    print(string[0:4])
    print("".join(string))


def time_parse():
    now = datetime.datetime.now()
    str_time = now.strftime("%m-%d %H:%M")
    print(">>>>> parse time:")
    with_year = "{year}-{suffix}".format(year="2017", suffix=str_time)
    print(with_year)
    new_time = datetime.datetime.strptime(with_year, "%Y-%m-%d %H:%M")
    print(">>>>> string to time:")
    print(new_time.timestamp())

def connect_mysql(**kwargs):
    options = {
        "host": kwargs.pop("host", "localhost"),
        "user": kwargs.pop("user", "root"),
        "password": kwargs.pop("password", "111111"),
        "database": kwargs.pop("database", "hahajok"),
        "port": kwargs.pop("port", 3306),
        "charset": kwargs.pop("charset", "utf8")
    }
    print(options)
    conn = MySQLdb.Connect(options)
    cursor = conn.cursor()
    cursor.execute("select * from user")
    result = cursor.fetchall()
    print(result)

def rand_test():
    a = random.randint(1, 1000)
    print(a)




def fetch_mysql():
    conn = MySQLdb.Connect(host="localhost", user="root", password="111111", db="hahajok", port=3306,
                           charset="utf8", cursorclass=DictCursor, autocommit=True)
    cursor = conn.cursor()
    sql = "insert into joker (id, title, content) values (1111, 'xixix', 'hahahhahah')"
    print(sql)
    cursor.execute(sql)
    result_set = cursor.fetchall()
    print(list(result_set))
    cursor.close()

def time_compute():

    now = datetime.datetime.now()
    now_timestamp = now.timestamp()
    print(">>>> now timestamp")
    print(now)
    print(now_timestamp)
    lastweek = now - datetime.timedelta(weeks=1)
    lastweek_timestamp = lastweek.timestamp()
    print(">>>>> last week timestamp")
    print(lastweek)
    print(lastweek_timestamp)



if __name__ == '__main__':
    # time_compute()
    # str_test()
    # time_parse()
    # fetch_mysql()
    # connect_mysql()
    # rand_test()

    l1 = [i for i in range(1, 100, 20)]
    print(l1)

