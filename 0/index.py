#-*- coding:utf-8 -*-

import tornado.wsgi


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write({'warning': 'fuck zhouquan!!!'})

app = tornado.wsgi.WSGIApplication([(r"/", MainHandler), ])
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
