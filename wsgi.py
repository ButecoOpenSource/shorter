#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.environ['AUTH_USER'] = ''
os.environ['AUTH_PWD'] = ''
os.environ['BITLY_TOKEN'] = ''
os.environ['BITLY_SHORTER_DOMAIN'] = ''

import tornado.wsgi
from server import application

if __name__ == '__main__':
    IP = os.environ.get('OPENSHIFT_PYTHON_IP', '0.0.0.0')
    PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8051))

    wsgi = tornado.wsgi.WSGIAdapter(application)
    server = wsgiref.simple_server.make_server(IP, PORT, wsgi)
    server.serve_forever()