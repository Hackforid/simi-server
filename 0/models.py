import hmac
import uuid
from hashlib import sha1
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Put your models here
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    cell_phone = Column(String(100))
    avatar_url = Column(String(100))
    first_login = Column(DateTime())
    last_login = Column(DateTime())
    is_active = Column(Boolean())
    access_token = Column(String(100))

    def __repr__(self):
        return '<Test: %d>' % self.id

    def check_password(self, password, encryption=lambda x: x):
        return encryption(password) == self.password

    def generate_key(self):
        unique = uuid.uuid4()
        self.access_token = hmac.new(unique.bytes, digestmod=sha1).hexdigest()
        return self.access_token


def init_db(engine):
    Base.metadata.create_all(bind=engine)
