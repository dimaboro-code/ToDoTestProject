from django.shortcuts import redirect
from rest_framework.exceptions import AuthenticationFailed

from .authentication import CookieJWTAuthentication


def home_redirect(request):
    jwt_auth = CookieJWTAuthentication()

    try:
        user_auth_tuple = jwt_auth.authenticate(request)
        if user_auth_tuple is not None:
            user, _ = user_auth_tuple
            if user.is_authenticated:
                return redirect('/tasks/')
    except AuthenticationFailed:
        pass

    return redirect('/auth/login/')
