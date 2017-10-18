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

class JWTMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', '')
        if not token.startswith('JWT'):
            return
        jwt_auth = JSONWebTokenAuthentication()
        auth = None
        try:
            auth = jwt_auth.authenticate(request)
        except Exception:
            return
        request.user = auth[0]
