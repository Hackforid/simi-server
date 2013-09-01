import tornado.web

from backend import Backend


class BaseHandler(tornado.web.RequestHandler):

    @property
    def backend(self):
        return Backend.instance()
