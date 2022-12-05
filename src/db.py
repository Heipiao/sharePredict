#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql,os

class Database():
    def __init__(self):
        self.mysql_host = os.getenv("MYSQL_HOST")
        self.mysql_port = int(os.getenv("MYSQL_PORT"))
        self.mysql_user = os.getenv("MYSQL_USER")
        self.mysql_password = os.getenv("MYSQL_PASSWD")

        self.user_table_conn = pymysql.connect(
                    host =  self.mysql_host , # 数据库地址
                    port = self.mysql_port,    # 数据库端口号
                    user=self.mysql_user ,    # 数据库账号
                    password=self.mysql_password,    # 数据库密码
                    db = 'usersInfo')    # 数据库表名
        # 创建数据库对象

        self.output_report_info_table_conn = pymysql.connect(
                    host =  self.mysql_host , # 数据库地址
                    port = self.mysql_port,    # 数据库端口号
                    user=self.mysql_user ,    # 数据库账号
                    password=self.mysql_password,    # 数据库密码
                    db = 'businessInfo')    # 数据库表名

    def get_user_info(self):
        db = self.user_table_conn.cursor()
        sql = "select username,email from all_user_info "
        db.execute(sql)
        result = db.fetchall()
        username = []
        email = []
        for res in result:
            username.append(res[0])
            email.append(res[1])
        db.close()
        return username,email
    
    def get_all_output_report_info_daily(self):
        db = self.output_report_info_table_conn.cursor()
        sql = "select share_daily_rise_summary from all_output_report_info_daily where create_time =   ( select MAX(create_time) from all_output_report_info_daily)"
        db.execute(sql)
        result = db.fetchall()
        db.close()
        return result[0][0]
     
      
if  __name__ == '__main__':
    Db = Database()
    print(Db.get_all_output_report_info_daily())