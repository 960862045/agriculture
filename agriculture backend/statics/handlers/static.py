from tornado.web import StaticFileHandler
from tornado.web import RequestHandler
from .base import BaseHandler


"""静态页面业务"""


class StaticFileHandler(StaticFileHandler):
    def __init__(self):
        pass


class IndexHandler(BaseHandler):
    def get(self):

        self.write("这是IndexHandler")