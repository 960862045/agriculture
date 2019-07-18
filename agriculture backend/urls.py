
from handlers import(
    find,
    user,
    static,
    input,
    admin
)
import config
import os

handlers = [(r'/$', static.IndexHandler),
            (r'/login', user.LoginHandler),
            (r'/find/origin', find.FindByOriHandler),
            (r'/find/product', find.FindByProHandler)

             # (r'^/()$', static.StaticFileHandler,
             # {"path":os.path.join(config.BASE_PATH, "statics/html"),
             # "default_filename":"index.html"})
        ]