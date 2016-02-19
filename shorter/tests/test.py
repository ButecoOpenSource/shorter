#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append('./')
sys.path.append('./../')

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from tornado.testing import AsyncHTTPTestCase, main

from shorter import bitly
from shorter import app


class MockBitly(object):
    def __init__(self, token, domain=None):
        pass

    def shorten(self, url):
        return 'http://short.url/KtYDG'

    def clicks(self, url):
        return 10

bitly.Bitly = MockBitly


class TestShorterApp(AsyncHTTPTestCase):

    def get_app(self):
        return app.ShorterApp(os.path.join(os.path.dirname(__file__), 'test.yml'))

    def test_index(self):
        response = self.fetch('/')
        self.assertEqual(response.headers['Content-Type'], 'text/html; charset=UTF-8')
        self.assertEqual(response.code, 200)
        self.assertTrue('domain.me' in str(response.body))

    def test_short(self):
        response = self.fetch('/short', method='POST', body=urlencode({'url': 'http://long.url/my-long-url'}))
        self.assertEqual(response.code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.body, b'"http://short.url/KtYDG"')

    def test_clicks(self):
        response = self.fetch('/clicks', method='POST', body=urlencode({'url': 'http://short.url/KtYDG'}))
        self.assertEqual(response.code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        self.assertEqual(response.body, b'10')

if __name__ == '__main__':
    main()
