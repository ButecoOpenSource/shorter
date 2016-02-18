#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.web
import yaml

from tornado.options import define, options

import handlers


define("config", default="shorter.yml", help="Configuration File")


class ShorterApp(tornado.web.Application):

    def __init__(self, config_file):
        url_patterns = [
            (r'/', handlers.IndexHandler),
            (r'/short', handlers.ShortHandler),
            (r'/clicks', handlers.ClicksHandler),
        ]
        settings = self.make_settings(config_file)
        super(ShorterApp, self).__init__(url_patterns, **settings)

    def listen(self):
        port = self.settings.get('server', {}).get('port', 8888)
        address = self.settings.get('server', {}).get('address', '127.0.0.1')
        server = super(ShorterApp, self).listen(port, address)

        print('Listening on http://%s:%d' % (address, port))

        if self.settings.get('debug', False):
            if self.settings.get('autoreload', False):
                print('Using autoreloader.')
            print('Press Ctrl-C to quit.')

        return server

    def make_settings(self, config_file):
        print('Loading config: %s' % config_file)

        settings = {
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'static_url_prefix': '/static/',
            'debug': False,
            'autoreload': False
        }

        with open(config_file, 'r') as f:
            settings.update(yaml.load(f))

        return settings

if __name__ == '__main__':
    tornado.options.parse_command_line()
    application = ShorterApp(options.config)
    application.listen()
    tornado.ioloop.IOLoop.instance().start()
