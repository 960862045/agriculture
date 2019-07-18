from peewee import (
    MySQLDatabase,
    Model,
)
import db
import config

"""根据数据库名称生成数据库配置信息"""
if config.settings.get("debug", "") == True:
    # 如果是测试状态使用本地数据库
    dbinfo = db.DB.get_dbconfig_by_name("LOCAL")
else:
    dbinfo = db.DB.get_dbconfig_by_name("MYSQL")

"""链接数据库"""

db = MySQLDatabase(**dbinfo)



class BaseModel(Model):

    class Meta:
        """指定数据库为db"""
        database = db

