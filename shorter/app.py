import os
import yaml

import tornado.ioloop
import tornado.web

from tornado.options import define, options

from . import handlers


define("config", default=None, help="Configuration File")


class ShorterApp(tornado.web.Application):
    def __init__(self, **settings):
        url_patterns = [
            (r"/", handlers.IndexHandler),
            (r"/status", handlers.StatusHandler),
            (r"/short", handlers.ShortHandler),
        ]

        app_settings = {
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "static_url_prefix": "/static/",
            "debug": False,
            "autoreload": False,
        }

        app_settings.update(settings)

        super(ShorterApp, self).__init__(url_patterns, **app_settings)

    def listen(self):
        port = self.settings.get("server", {}).get("port", 8888) or 8888
        address = (
            self.settings.get("server", {}).get("address", "127.0.0.1") or "127.0.0.1"
        )
        server = super(ShorterApp, self).listen(port, address)

        print("Listening on http://%s:%d" % (address, port))

        if self.settings.get("debug", False):
            if self.settings.get("autoreload", False):
                print("Using autoreloader.")
            print("Press Ctrl-C to quit.")

        return server


def make_settings(config_file):
    if config_file is None:
        print("Loading config from ENV")

        return {
            "debug": False,
            "autoreload": False,
            "compress_response": True,
            "xsrf_cookies": True,
            "server": {
                "port": os.getenv("SERVER_PORT"),
                "address": os.getenv("SERVER_ADDRESS"),
            },
            "bitly": {
                "branded_domain": os.getenv("BITLY_DOMAIN"),
                "access_token": os.getenv("BITLY_TOKEN"),
            },
        }

    print("Loading config: %s" % config_file)

    with open(config_file, "r") as f:
        return yaml.load(f)


def run():
    tornado.options.parse_command_line()
    settings = make_settings(options.config)
    application = ShorterApp(**settings)
    application.listen()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    run()
