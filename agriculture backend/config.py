import os

BASE_PATH = os.path.dirname(__file__)

# Application配置参数
settings = {
    "static_path":os.path.join(BASE_PATH, "statics"),
    "login_url":'/login',
    "debug":True,

}

# mysql配置
mysql_options = {
    "host":"192.168.68.1",
    "database":"argi_analysis",
    "user":"root",
    "password":"mysql"
}





