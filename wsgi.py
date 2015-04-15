#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.environ['REQUIRE_AUTH'] = False
os.environ['AUTH_USER'] = ''
os.environ['AUTH_PWD'] = ''
os.environ['BITLY_TOKEN'] = ''
os.environ['BITLY_SHORTER_DOMAIN'] = ''
os.environ['STATIC_FOLDER'] = './static'

import tornado.ioloop
import tornado.wsgi
import wsgiref.simple_server
from server import application as srv

application = tornado.wsgi.WSGIAdapter(srv)

if __name__ == '__main__':
    IP = os.environ.get('OPENSHIFT_PYTHON_IP', '0.0.0.0')
    PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8051))
    #srv.listen(PORT , IP)
    #tornado.ioloop.IOLoop.instance().start()
    server = wsgiref.simple_server.make_server(IP, PORT, application)
    server.serve_forever()
