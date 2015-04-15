#!/usr/bin/env python
# -*- coding: utf-8 -*-

import handlers
import tornado.web
import os

STATIC_FOLDER = os.getenv('STATIC_FOLDER', r'./static')

routes = [
    (r'/', tornado.web.RedirectHandler, {'url':'/index.html'}),
    (r'/(favicon.ico)', tornado.web.StaticFileHandler, {'path': STATIC_FOLDER + '/img'}),
    (r'/short', handlers.UrlShorterHandler),
    (r'/(.*\.html)', handlers.StaticFileHandler, {'path': STATIC_FOLDER}),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': STATIC_FOLDER}),
]