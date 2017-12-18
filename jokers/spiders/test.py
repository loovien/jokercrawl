# -*- coding: utf-8 -*-


import datetime


def time_parse():
    now = datetime.datetime.now()
    str_time = now.strftime("%m-%d %H:%M")
    print(">>>>> parse time:")
    with_year = "{year}-{suffix}".format(year="2017", suffix=str_time)
    print(with_year)
    new_time = datetime.datetime.strptime(with_year, "%Y-%m-%d %H:%M")
    print(">>>>> string to time:")
    print(new_time.timestamp())


if __name__ == '__main__':
    time_parse()
