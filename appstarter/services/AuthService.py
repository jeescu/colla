from appstarter.models import Authentication
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from datetime import timedelta
from appstarter import config
from appstarter.utils import ResponseParcel


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

    def authenticate(self, request):
        auth = AuthService(request)
        parcel = ResponseParcel.ResponseParcel()

        access_token = Authentication.objects.get(access_token=auth.__session_token)

        if access_token is not None:
            if access_token.expired_at > timezone.now():
                return
            else:
                access_token.delete()

        parcel.set_uri('/colla')
        return parcel.redirect()

    def authorize(self, request):
        pass

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
