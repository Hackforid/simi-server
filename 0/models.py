from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Put your models here
class User(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    cell_phone = Column(String(100))
    avatar_url = Column(String(100))
    first_login = Column(DateTime())
    last_login = Column(DateTime())
    is_active = Boolean()

    def __repr(self):
        return '<Test: %d>' % self.id


def init_db(engine):
    Base.metadata.create_all(bind=engine)
