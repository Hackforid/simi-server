from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import options


class Backend(object):

    def __init__(self):
        engine = create_engine(
            "mysql://{0}:{1}@{2}/{3}".format(
                options.mysql_user, options.mysql_pass, options.mysql_host, options.mysql_db))
        self._engine = engine
        self._session = sessionmaker(bind=engine)

    @classmethod
    def instance(cls):
        """Singleton like accessor to instantiate backend object"""
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def get_session(self):
        return self._session()

    def get_engine(self):
        return self._engine
