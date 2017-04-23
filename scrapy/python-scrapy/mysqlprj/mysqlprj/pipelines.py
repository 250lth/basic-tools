# -*- coding: utf-8 -*-
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MysqlprjPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="250lth", db="mypydb")

    def process_item(self, item, spider):
        name = item["name"][0]
        key = item["keywd"][0]
        sql = "INSERT INTO mytb(title, keywd) VALUES('"+ name +"','" + key +"')"
        self.conn.query(sql)
        return item
