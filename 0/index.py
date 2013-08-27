#-*- coding:utf-8 -*-

import tornado.wsgi
import tornado


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(tornado.version)

app = tornado.wsgi.WSGIApplication([(r"/", MainHandler), ])
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
