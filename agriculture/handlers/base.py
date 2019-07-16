from tornado.web import RequestHandler
import json

class BaseHandler(RequestHandler):
    """handler基类"""
    def prepare(self):
        """预解析json数据"""
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = {}

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        """设置默认json格式"""
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def on_finish(self):
        pass

    def get_current_user(self):
        pass
