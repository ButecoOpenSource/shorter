#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unirest
from urllib import quote

BITLY_API_URL = 'https://api-ssl.bitly.com'
BITLY_SHORTER_URL = BITLY_API_URL + '/v3/shorten'

class ShorterException(Exception):
    pass

class Shorter(object):

    def __init__(self, token, domain=None):
        if not token:
            raise ValueError('You must provide a valid access token.')

        self.token = token
        self.domain = domain or ''

    def generate(self, long_url):
        if not long_url:
            raise ShorterException('"long_url" must be not empty.')

        long_url = quote(long_url)
        response = unirest.get(BITLY_SHORTER_URL, params={
            'domain': self.domain,
            'access_token': self.token,
            'longUrl': long_url,
            'format': 'json'
        })

        if response.code == 200 and response.body.get('status_code') == 200:
            return response.body.get('data', {}).get('url', long_url)
        else:
            raise ShorterException(response.body)

if __name__ == '__main__':
    S = Shorter('YOUR_KEY')
    url = S.generate('https://google.com')
    print(url)