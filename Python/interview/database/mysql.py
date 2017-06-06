# -*- coding: UTF-8 -*-
import MySQLdb

class connect_to_mysql(object):
    def connect_to_db(self, user_name, password, database):
        # 打开数据库连接

        db = MySQLdb.connect("localhost", user_name, password, database)

        # 使用cursor()方法获取操作游标

        cursor = db.cursor()

        # 使用fetchone()方法获取一条数据库

        data = cursor.fetchone()

        print "Database version: %s" % data

        # 关闭数据库
        db.close()

