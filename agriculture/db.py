import os
import configparser
"""从config.ini读取数据库信息，转化为字典格式"""

class DB():

    @classmethod
    def get_dbconfig_by_name(cls, dbname):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.path.dirname(__file__), "config.ini"))
        host = config.get(dbname, "host")
        port = config.get(dbname, "port")
        user = config.get(dbname, "user")
        password = config.get(dbname, "password")
        database = config.get(dbname, "database")
        return {"host":host, "port":int(port), "user":user, "password": password, "database": database}