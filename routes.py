#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import handlers

routes = [
    (r'/', tornado.web.RedirectHandler, {'url':'/index.html'}),
    (r'/(favicon.ico)', tornado.web.StaticFileHandler, {'path': r'./static/img'}),
    (r'/short', handlers.UrlShorterHandler),
    (r'/(.*\.html)', handlers.StaticFileHandler, {'path': r'./static'}),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': r'./static'}),
]