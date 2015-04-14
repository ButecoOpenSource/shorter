#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import tornado.web

from auth import require_basic_auth, check_credentials
from bitly import Shorter, ShorterException

BITLY_TOKEN = os.getenv('BITLY_TOKEN', '')
BITLY_SHORTER_DOMAIN = os.getenv('BITLY_SHORTER_DOMAIN', '')
REALM = 'Shorter Login'

@require_basic_auth(check_credentials, realm=REALM)
class StaticFileHandler(tornado.web.StaticFileHandler):
    pass

@require_basic_auth(check_credentials, realm=REALM)
class UrlShorterHandler(tornado.web.RequestHandler):

    def get(self):
        long_url = self.get_argument('url', '')

        if long_url:
            S = Shorter(BITLY_TOKEN, BITLY_SHORTER_DOMAIN)

            try:
                url = S.generate(long_url)
            except ShorterException as e:
                self.set_status(400)
                self.set_header('Content-Type', 'application/json')
                self.write(json.dumps(e.message))
            except Exception:
                self.set_status(500)
                self.set_header('Content-Type', 'application/json')
                self.write(json.dumps({'message': 'Unknown error.'}))
            else:
                self.set_header('Content-Type', 'application/json')
                self.write(json.dumps(url))
        else:
            self.set_status(400)
            self.set_header('Content-Type', 'application/json')
            self.write(json.dumps({
                'status_code': 500,
                'data': [],
                'status_txt': 'INVALID_URI'
            }))
