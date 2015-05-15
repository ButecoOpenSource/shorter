# -*- coding: utf-8 -*-

import handlers
import tornado.web

from settings import STATIC_ROOT, STATIC_MEDIA_ROOT


url_patterns = [
    (r'/', tornado.web.RedirectHandler, {'url':'/index.html'}),
    (r'/(favicon.ico)', handlers.StaticFileHandler, {'path': STATIC_MEDIA_ROOT}),
    (r'/short', handlers.UrlShorterHandler),
    (r'/(.*\.html)', handlers.StaticFileHandler, {'path': STATIC_ROOT}),
    (r'/(.*)', handlers.StaticFileHandler, {'path': STATIC_ROOT}),
]
