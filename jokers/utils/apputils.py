# -*- coding: utf-8 -*-
# author: luowen<bigpao.luo@gmail.com>
# time: 2017/12/19 0:37
# desc:  string process util

import datetime


def strip_value(string, char):
    """ strip special char """
    if string is not None and len(string) > 0:
        return str.strip(string, char)
    return string


def parse_strtime(string, fmt):
    datetime_obj = datetime.datetime.strptime(string, fmt)
    return datetime_obj.timestamp()


if __name__ == "__main__":
    print(int(parse_strtime("2017-11-12", "%Y-%m-%d")))
