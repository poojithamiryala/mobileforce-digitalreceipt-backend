from datetime import time

import jwt
from django.http import HttpResponseForbidden

from digitalReceipt import settings


class AuthorizationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwtEscapeUrls = ['/v1/user/otp_register',
                         '/v1/user/register']
        if request.path in jwtEscapeUrls:
            response = self.get_response(request)
            return response
        else:
            return self.process_view(request)  # Call process_request()

    def process_view(self, request, view_func, view_args, view_kwargs):
        header_token = request.META.get('token', None)
        if header_token is not None:
            try:
                vaildate_token = jwt.decode(header_token, settings.SECRET_KEY, algorithm='HS256')
                if time.time() < vaildate_token['exp']:
                    request.user = vaildate_token['user']
                    response = self.get_response(request)
                    return response
                else:
                    return HttpResponseForbidden("Token got expired.Login again")
            except Exception as error:
                return HttpResponseForbidden("Login failed")
