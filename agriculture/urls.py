from handlers import static
from handlers import find
from handlers import user
import config
import os

handlers = [(r'/$', static.IndexHandler),
            (r'/login', user.LoginHandler)
            # (r'^/()$', static.StaticFileHandler,
             # {"path":os.path.join(config.BASE_PATH, "statics/html"),
             # "default_filename":"index.html"})
        ]