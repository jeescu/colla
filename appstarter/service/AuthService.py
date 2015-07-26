from appstarter.models import Authentication


class AuthService(object):
    __user_id = 0
    __token = ""

    def __init__(self, id, token):
        self.__user_id = id
        self.__token = token

    def get_auth_token(self):
        return self.__token

    def set_auth_token(self, auth):
        self.__token = auth.access_token
        self.__user_id = auth.user_id

    # @TODO: put username, password auth here
    def authenticate(self, request):
        pass

    def is_authenticated(self):
        check_token = Authentication.objects.get(access_token=self.__token)

        if check_token is not None:
            return check_token.user_id == self.__user_id
        else:
            return False
