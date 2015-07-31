from appstarter.models import Authentication
from django.utils import timezone
from datetime import timedelta
from appstarter import config


class AuthService(object):
    __app_config = config
    __user = None
    __auth = None
    __request = None
    __session_token = None

    def __init__(self, request):
        self.__request = request

        request_session = self.__request.COOKIES
        self.__session_token = request_session.get('sessionid') or request_session.get('csrftoken')

    def set_user(self, user):
        self.__user = user

    def set_token(self, auth):
        self.__auth = auth

    def get_token(self):
        return self.__session_token

    def is_authenticated(self):
        is_auth = False
        check_token = Authentication.objects.get(access_token=self.__auth.access_token)

        if check_token is not None:
            if check_token.expired_at > timezone.now():
                is_auth = check_token.user_id == self.__user.id

        else:
            is_auth = False

        return is_auth

    def add_session(self):
        authenticated_user = Authentication(
            user_id=self.__user.id,
            provider=self.__request.GET.get('provider'),
            provider_user_id=self.__request.GET.get('id'),
            access_token=self.__session_token,
            expired_at=timezone.now() + timedelta(hours=self.__app_config.expires)
        )
        authenticated_user.save()

    def end_session(self):
        auth_user = Authentication.objects.get(access_token=self.__session_token)
        auth_user.delete()
