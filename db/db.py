import os

import pymysql
import yaml
from  utils.singleton import singleton

@singleton
class DB:
    def __init__(self):
        print('初始化')

        # 读取配置文件
        # C:\Users\lv\Desktop\fangjindong\fangJD\config\db.yaml
        current_path = os.getcwd()

        # filename = moduele_path + '../config/db.yaml'
        with open( current_path + "/config/db.yaml", "r") as f:
            data = yaml.safe_load(f)
        # # 打开数据库连接
        self.db = pymysql.connect(**data)

    # 数据库执行 SQL
    def executeSql(self, SQL):
        # 使用 execute() 执行 SQL 查询
        cursor = self.db.cursor()
        cursor.execute(SQL)
        # 获取所有记录列表
        results = cursor.fetchall()
        return results

    # 数据库连接关闭
    def close(self):
        print('关闭数据库')
        self.db.close()


db = DB()


