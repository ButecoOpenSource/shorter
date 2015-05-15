# -*- coding: utf-8 -*-

import os


BITLY_API_URL = 'https://api-ssl.bitly.com'
BITLY_SHORTER_URL = BITLY_API_URL + '/v3/shorten'
BITLY_TOKEN = os.getenv('BITLY_TOKEN', '')
BITLY_SHORTER_DOMAIN = os.getenv('BITLY_DOMAIN', '')

STATIC_ROOT = os.getenv('STATIC_FOLDER', r'./static')
STATIC_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'img')

AUTH_USER = os.getenv('AUTH_USER', '')
AUTH_PWD = os.getenv('AUTH_PWD', '')

settings = {
    'debug': False,
    'cookie_secret': 'U2hvcnRlciBVcmwgQ29va2llIFNlY3JldA==',
    'xsrf_cookies': True,
    'serve_traceback': True,
}
