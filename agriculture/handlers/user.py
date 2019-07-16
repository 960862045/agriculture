from .base import BaseHandler
import re
from models.user import User

"""用户基本业务"""

class LoginHandler(BaseHandler):
    """登录"""
    def get(self):
        pass

    def post(self):
        # 获取用户名，密码
        username = self.get_argument("name", "")
        password = self.get_argument("password", "")
        # 判断用户名，密码是否为空
        if not all([username, password]):
            return self.write("参数错误")
        # 通过用户名向数据库查询, 返回查询到的对象
        try:
            user = User.get(User.name == username)

            # user = User.select().where(User.name == username).get()
        except Exception as f:
            user = User()
        # 根据查询对象的密码进行比对

        if user.password == password:
            # 设置安全cookie，表示用户已经登录
            self.set_secure_cookie("login", user.name)
            self.write("oh, %s! you have logined successfully!" %user.name)
        else:
            self.write("用户名或密码错误")


class RegisterHandler(BaseHandler):
    """注册"""
    def get(self):
        pass

    def post(self):
        pass


class CheckLoginHandler(BaseHandler):
    """检验是否登录"""
    def get(self):
        pass

    def post(self):
        pass


class LogoutHandler(BaseHandler):
    """退出登录"""
    def get(self):
        pass

    def post(self):
        pass


class ModifyPassWDHandler(BaseHandler):
    """修改密码"""
    def get(self):
        pass

    def post(self):
        pass


