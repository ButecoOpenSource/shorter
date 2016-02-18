#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import tornado.web

from bitly import Bitly, BitlyException


class ShortHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def get(self):
        settings = self.application.settings.get('bitly', {})
        token = settings.get('access_token', '')
        domain = settings.get('branded_domain', None)

        long_url = self.get_argument('url', '')

        if long_url:
            bitly = Bitly(token, domain)

            try:
                short_url = bitly.shorten(long_url)
            except BitlyException as e:
                self.set_status(400)
                self.write(json.dumps(e.payload))
            except Exception as e:
                self.set_status(500)
                self.write(json.dumps({'message': str(e)}))
            else:
                self.set_status(200)
                self.write(json.dumps(short_url))
        else:
            self.set_status(400)
            self.write(json.dumps({
                'status_code': 500,
                'data': [],
                'status_txt': 'INVALID_URI'
            }))


class ClicksHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def get(self):
        settings = self.application.settings.get('bitly', {})
        token = settings.get('access_token', '')
        domain = settings.get('branded_domain', None)

        short_url = self.get_argument('url', '')

        if short_url:
            bitly = Bitly(token, domain)

            try:
                count = bitly.clicks(short_url)
            except BitlyException as e:
                self.set_status(400)
                self.write(json.dumps(e.payload))
            except Exception as e:
                self.set_status(500)
                self.write(json.dumps({'message': str(e)}))
            else:
                self.set_status(200)
                self.write(json.dumps(count))
        else:
            self.set_status(400)
            self.write(json.dumps({
                'status_code': 500,
                'data': [],
                'status_txt': 'INVALID_URI'
            }))


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
