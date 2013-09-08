# -*- coding: utf-8 -*-
import json


class JsonValidateMessagesMixin(object):
    default_message = ''

    def validate_filed_exist(self, key):
        value = self.request_json.get(key, None)
        if not value:
            self.default_error_message += "%s is required;" % key


class JsonRequestResponseMixin(JsonValidateMessagesMixin):

    """
    Extends JSONResponseMixin.  Attempts to parse request as JSON.  If request
    is properly formatted, the json is saved to self.request_json as a Python
    object.  request_json will be None for imparsible requests.
    Set the attribute require_json to True to return a 400 "Bad Request" error
    for requests that don't contain JSON.

    Note: To allow public access to your view, you'll need to use the
    csrf_exempt decorator or CsrfExemptMixin.

    Example Usage:

        class SomeView(CsrfExemptMixin, JsonRequestResponseMixin):
            def post(self, request, *args, **kwargs):
                do_stuff_with_contents_of_request_json()
                return self.render_json_response(
                    {'message': 'Thanks!'})
    """

    require_json = True
    error_response_dict = {u"errors": [u"Improperly formatted request"]}

    def json_validate(self):
        error_dict = {}
        return error_dict

    def render_bad_request_response(self, error_dict=None):
        if error_dict is None:
            error_dict = self.error_response_dict
        self.set_status(400)
        self.finish(error_dict)

    def get_request_json(self):
        try:
            return json.loads(self.request.body)
        except ValueError:
            return None

    def prepare(self, request, *args, **kwargs):
        self.request_json = self.get_request_json()
        if self.require_json and self.request_json is None:
            self.render_bad_request_response()
        error_dict = self.json_validate()
        if error_dict:
            self.render_bad_request_response(error_dict)
        return super(JsonRequestResponseMixin, self).prepare()
