import tornado.web
import tornado.ioloop

from urls import handlers
import os
import config

# class Application(tornado.web.Application):
#     def __init__(self, *args, **kwargs):
#         super(Application, self).__init__(*args, **kwargs)


def main():
    app = tornado.web.Application(handlers,cookie_secret = "pTlLhm9kSrCAA6Ik74E1kSG9YDExq0dbq7zdXm+M3s0=",)
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()