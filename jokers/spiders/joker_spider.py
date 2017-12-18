# -*- coding: utf-8 -*-
# @author: luowen<bigpao.luo@gmail.com>
# @desc: joker spider main class
# @time: 2017-12-18 15:44

import scrapy
import time
from jokers.utils.apputils import *


class JokerSpider(scrapy.Spider):
    name = "joker"

    start_urls = [
        "http://neihanshequ.com/"
    ]

    def parse(self, response):
        strip_char = "\n\t"
        for item in response.css("ul#detail-list li .detail-wrapper"):
            date_str = strip_value(item.css(".time::text").extract_first(), strip_char)
            timestamp = time.time()
            if date_str is not "":
                timestamp = parse_strtime("2017-{}".format(date_str), "%Y-%m-%d %H:%M")
            joker = {
                "avatar": strip_value(item.css("a > img::attr(data-src)").extract_first(), strip_char),
                "nickname": strip_value(item.css(".name::text").extract_first(), strip_char),
                "createdAt": int(timestamp),
                "content": strip_value(item.css("p::text").extract_first(), strip_char),
                "id": strip_value(item.css(".options::attr(data-group-id)").extract_first(), strip_char),
            }
            self.logger.info("处理的信息", joker)
            yield joker
