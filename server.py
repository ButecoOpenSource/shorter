import json
import os
import tornado.ioloop
import tornado.web

from bitly import Shorter, ShorterException

BITLY_TOKEN = os.getenv('BITLY_TOKEN', '')
BITLY_SHORTER_DOMAIN = os.getenv('BITLY_SHORTER_DOMAIN', '')

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


application = tornado.web.Application([
    (r'/', tornado.web.RedirectHandler, {'url':'/index.html'}),
    (r'/short', UrlShorterHandler),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': r'./static'}),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()