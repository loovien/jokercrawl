# -*- coding: utf-8 -*-
# author: luowen<bigpao.luo@gmail.com>
# time: 2017/12/19 21:28
# desc:
import json
import scrapy
import datetime


class JokersSpider(scrapy.Spider):
    name = "neihan"
    def start_requests(self):
        crawl_url = 'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time='
        step = 1800 # 30 minute as page

        now_date = datetime.datetime.now()
        now_timestamp = now_date.timestamp()
        lastweek_date = now_date - datetime.timedelta(weeks=1)
        lastweek_timestamp = lastweek_date.timestamp()

        def build_urls(timestamp):
            return crawl_url + str(timestamp)
        start_urls = list(map(build_urls, [i for i in range(int(lastweek_timestamp), int(now_timestamp), step)]))
        request_list = []
        for url in start_urls[0:10]:
            request_list.append(scrapy.Request(url=url))
        return request_list

    def parse(self, response):

        json_resp = json.loads(response.body, encoding="utf-8")
        joker_list = json_resp.get("data", {}).get("data")
        if joker_list is None:
            return

        try:
            for joker in joker_list:
                item = {
                    "id": "{}_{}".format(self.name, joker.get("group", {}).get("id")),
                    "uid": joker.get("group", {}).get("user", {}).get("user_id"),
                    "nickname": joker.get("group", {}).get("user", {}).get("name"),
                    "avatar": joker.get("group", {}).get("user", {}).get("avatar_url"),
                    "title": joker.get("group", {}).get("text"),
                    "content": joker.get("group", {}).get("content"),
                    "createdAt": joker.get("group", {}).get("create_time")
                }
                self.logger.info("处理对象: {}".format(item))
                yield item
        except Exception as e:
            self.logger.error("处理数据发生错误: %s" % e)
