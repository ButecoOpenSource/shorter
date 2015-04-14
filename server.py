#!/usr/bin/env python
# -*- coding: utf-8 -*-

import routes
import tornado.ioloop
import tornado.web

settings = {
    'debug': False,
    'cookie_secret': 'U2hvcnRlciBVcmwgQ29va2llIFNlY3JldA==',
    'xsrf_cookies': True,
}

application = tornado.web.Application(routes.routes, **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()