# -*- coding: utf-8 -*-
# @author: luowen<bigpao.luo@gmail.com>
# @desc: joker spider main class
# @time: 2017-12-18 15:44

import scrapy


class JokerSpider(scrapy.Spider):
    name = "joker"

    start_urls = [
        "http://neihanshequ.com/"
    ]

    def parse(self, response):
        def strip_value(value):
            if value is not None and len(value) > 0:
                return value.strip("\n\t")
            return value

        for item in response.css("ul#detail-list li .detail-wrapper"):
            joker = {
                "avatar": strip_value(item.css("a > img::attr(data-src)").extract_first()),
                "nickname": strip_value(item.css(".name::text").extract_first()),
                "createdAt": strip_value(item.css(".time::text").extract_first()),
                "content": strip_value(item.css("p::text").extract_first()),
                "id": strip_value(item.css(".options::attr(data-group-id)").extract_first()),
            }
            self.logger.info("处理的信息", joker)
            yield joker
