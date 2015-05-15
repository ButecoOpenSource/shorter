#!/usr/bin/env python
# -*- coding: utf-8 -*-

import auth
import json
import tornado.web

from bitly import Bitly, BitlyException
from settings import BITLY_TOKEN, BITLY_SHORTER_DOMAIN, AUTH_USER, AUTH_PWD


def check_credentials(user, pwd):
    if AUTH_USER == AUTH_PWD == '':
        return True

    return user == AUTH_USER and pwd == AUTH_PWD

@auth.basic(check_credentials)
class StaticFileHandler(tornado.web.StaticFileHandler):
    pass

@auth.basic(check_credentials)
class UrlShorterHandler(tornado.web.RequestHandler):

    def get(self):
        long_url = self.get_argument('url', '')

        if long_url:
            S = Bitly(BITLY_TOKEN, BITLY_SHORTER_DOMAIN)

            try:
                url = S.shorten(long_url)
            except BitlyException as e:
                self.set_status(400)
                self.set_header('Content-Type', 'application/json')
                self.write(json.dumps(e.message))
            except Exception as e:
                self.set_status(500)
                self.set_header('Content-Type', 'application/json')
                self.write(json.dumps({'message': str(e)}))
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
