# -*- coding: utf-8 -*-
from datetime import datetime
from tornado.web import RequestHandler

from mixins import JsonRequestResponseMixin

from models import User


class BaseHandler(RequestHandler):

    @property
    def db(self):
        return self.application.db


class LoginHandler(BaseHandler, JsonRequestResponseMixin):

    def json_validate(self):
        error_dict = {}

        self.validate_field_exist('cell_phone')
        self.validate_filed_exist('password')

        if self.default_error_message:
            error_dict['message'] = self.default_error_message
            return error_dict
        else:
            return {}

    def post(self):
        cell_phone = self.request_json['cell_phone']
        password = self.request_json['password']
        user = self.db.query(User).filter_by(cell_phone=cell_phone).first()
        if user:
            if user.check_password(password):
                user.last_login = datetime.now()
                token_dict = {'access_token': user.generate_key()}
                self.db.commit()
                self.write(token_dict)
            else:
                pass
        else:
            pass
