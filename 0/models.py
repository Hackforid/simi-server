from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from backend import Backend

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    password = Column(String(100))
    cell_phone = Column(String(100))

    def __repr__(self):
        return "<User('%s', '%s', '%s')> % (self.name, self.fullname, self.password)"


Base.metadata.create_all(Backend.instance().get_engine())
