import logging

from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# class JWTMiddleware(object):
#     def process_view(self, req, view_func, view_args, view_kwargs):
#         token = req.META.get('HTTP_AUTHORIZATION', '')
#         if not token.startswith('JWT'):
#             return
#         jwt_auth = JSONWebTokenAuthentication()
#         auth = None
#         try:
#             auth = jwt_auth.authenticate(req)
#         except Exception:
#             # TODO: this seems dangerous; double-check that this is acceptable
#             return
#         req.user = auth[0]

logger = logging.getLogger('django')

class JWTMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        logger.info("MIDDLEWARE: middleware running")

        token = request.META.get('HTTP_AUTHORIZATION', '')
        if not token.startswith('JWT'):
            logger.debug("MIDDLEWARE: Token did not start with 'JWT'"
            "\nToken: %s" %(token))
            return
        jwt_auth = JSONWebTokenAuthentication()
        auth = None
        try:
            auth = jwt_auth.authenticate(request)
        except Exception as err:
            logger.exception("MIDDLEWARE: Authentication of jwt token did not work;"
            "\nError: %s"
            "\nToken: %s"
            % (err, token))
            return
        request.user = auth[0]
        logger.info("MIDDLEWARE: Request.user is %s" % (request.user))
