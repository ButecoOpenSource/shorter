#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import os

from tornado.concurrent import Future

USER = os.getenv('AUTH_USER', '')
PWD = os.getenv('AUTH_PWD', '')

def require_basic_auth(validate_func=lambda *args, **kwargs: True, realm='Restricted'):
    def require_basic_auth_decorator(handler_class):
        def wrap_execute(handler_execute):
            def require_basic_auth(handler, kwargs):
                def create_auth_header():
                    handler.set_status(401)
                    handler.set_header('WWW-Authenticate', 'Basic realm=%s' % realm)
                    handler._transforms = []
                    handler.finish()
                    return False

                auth_header = handler.request.headers.get('Authorization')
                if auth_header is None or not auth_header.startswith('Basic '):
                    return create_auth_header()
                else:
                    auth_decoded = base64.decodestring(auth_header[6:])
                    user, pwd = auth_decoded.split(':', 2)
                    if validate_func(user, pwd):
                        handler.user = user
                        return True
                    else:
                        return create_auth_header()

            def _execute(self, transforms, *args, **kwargs):
                if not require_basic_auth(self, kwargs):
                    return Future()

                return handler_execute(self, transforms, *args, **kwargs)
            return _execute

        handler_class._execute = wrap_execute(handler_class._execute)
        return handler_class
    return require_basic_auth_decorator

def check_credentials(user, pwd):
    return user == USER and pwd == PWD