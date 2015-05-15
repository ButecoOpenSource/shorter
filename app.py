#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urls
import tornado.ioloop
import tornado.web

from settings import settings


application = tornado.web.Application(urls.url_patterns, **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
