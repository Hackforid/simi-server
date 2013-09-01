from base_handler import BaseHandler

import tornado.ioloop
import tornado.web

from models import User


class ExampleHandler(BaseHandler):

    def get(self):
        session = self.backend.get_session()
        try:
            user = User(name='ed', fullname='ed fuck', password='edspassword')
            session.add(user)
            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()

application = tornado.web.Application([(r"/", ExampleHandler), ])
if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
