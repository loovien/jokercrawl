# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import time
from MySQLdb.cursors import DictCursor
import random


class JokersPipeline(object):

    connection = None

    def __init__(self, **kwargs):
        self.host = kwargs.pop("host", "localhost")
        self.user = kwargs.pop("user", "root")
        self.password = kwargs.pop("password", "111111")
        self.database = kwargs.pop("database", "hahajok")
        self.port = kwargs.pop("port", 3306)
        self.charset = kwargs.pop("charset", "utf8")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get("MYSQL_HOST"),
            user=crawler.settings.get("MYSQL_USER"),
            password=crawler.settings.get("MYSQL_PWD"),
            database=crawler.settings.get("MYSQL_DATABASE"),
            port=crawler.settings.get("MYSQL_PORT"),
            charset=crawler.settings.get("MYSQL_CHARSET"),
        )

    def open_spider(self, spider):
        try:
            self.connection = MySQLdb.Connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                charset=self.charset,
                cursorclass=DictCursor,
                autocommit=True
            )
        except Exception as e:
            spider.logger.info("连接数据库状态: {}".format(e))

    def process_item(self, item, spider):
        spider.logger.info("处理item: {}".format(item))
        if item.get("content", None) is None:
            spider.logger.info("过滤内容为空item: {}".format(item))
            return
        self.record_jokers(item, spider)
        self.record_user(item, spider)

    def record_jokers(self, item, spider):
        sectime = time.time()
        timestamp = int(sectime)
        content = list(item.get("content", ""))
        id = item.get("id", int(sectime * 1000))
        uid = random.randint(1, 1000)
        sql = "INSERT INTO joker (uniqueId, uid, classId, title, content, status, createdAt, passedAt, updatedAt)" \
              " values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
        sql = sql.format(id, uid, 1, "".join(content[0:40]), "".join(content), 1,
                         timestamp, timestamp, timestamp)
        spider.logger.info("jokersql: {}".format(sql))
        cursor = self.connection.cursor()
        try:
            stat = cursor.execute(sql)
            spider.logger.info("插入数据表joker: {}".format(stat))
            cursor.close()
        except Exception as e:
            spider.logger.error("插入数据表joker错误: {}".format(e))
            pass

    def record_user(self, item, spider):
        sectime = time.time()
        timestamp = int(sectime)
        sql = "INSERT INTO user (unionId, openId, nickname, avatar, issave, createdAt, updatedAt)" \
              " values ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"
        sql = sql.format(item.get("id", int(sectime * 1000)), item.get("uid", 0), item.get("nickname"),
                         item.get("avatar"), 1, timestamp, timestamp)
        spider.logger.info("usersql: {}".format(sql))
        cursor = self.connection.cursor()
        try:
            stat = cursor.execute(sql)
            spider.logger.info("插入数据表user: {}".format(stat))
            cursor.close()
        except Exception as e:
            spider.logger.error("插入数据表userr错误: {}".format(e))
            pass

    def close_spider(self, spider):
        if self.connection is not None:
            stat = self.connection.close()
            spider.logger.info("关闭数据库连接: {}".format(stat))
