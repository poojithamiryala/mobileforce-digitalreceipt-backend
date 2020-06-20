import time

import jwt
from django.http import HttpResponseForbidden

from digitalReceipt import settings


class AuthorizationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwtEscapeUrls = ['/v1/user/otp_register',
                         '/v1/user/register','/v1/user/login']
        if request.path in jwtEscapeUrls:
            print("text122")
            response = self.get_response(request)
            return response
        else:
            header_token = request.META.get('HTTP_TOKEN', None)
            if header_token is not None:
                try:
                    vaildate_token = jwt.decode(header_token, settings.SECRET_KEY, algorithm='HS256')
                    if time.time() < vaildate_token['exp']:
                        request.user_id = vaildate_token['id']
                        response = self.get_response(request)
                        print(response)
                        return response
                    else:
                        return HttpResponseForbidden("Token got expired.Login again")
                except Exception as error:
                    return HttpResponseForbidden(error)
            else:
                return HttpResponseForbidden("Invalid credentails")

