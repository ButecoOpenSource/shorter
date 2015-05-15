#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import urls

from settings import settings
from tornado.options import define, options

define("port", default="5000", help="Port")

application = tornado.web.Application(urls.url_patterns, **settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
