from appstarter.models import Authentication
from django.utils import timezone

class AuthService(object):

    def __init__(self):
        pass

    def get_auth_token(self):
        return self.__token

    def set_auth_token(self, auth):
        self.__token = auth.access_token
        self.__user_id = auth.user_id

    # @TODO: put username, password auth here
    def authenticate(self, request):
        pass

    def is_authenticated(self, ):
        check_token = Authentication.objects.get(access_token=self.__token)

        if check_token is not None:
            if check_token.expired_at > timezone.now():
                return check_token.user_id == self.__user_id

        return False

    def end_session(self, request):
        author_request = request.COOKIES
        session_id = author_request.get('sessionid') or author_request.get('csrftoken')
        auth_user = Authentication.objects.get(access_token=session_id)
        auth_user.delete()
