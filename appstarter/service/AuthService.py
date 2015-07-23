__author__ = 'john'

from appstarter.models import Authentications

class AuthService(object):
    __user_id = 0
    __token = ""

    def __init__(self, id, token):
        self.__user_id = id
        self.__token = token

    def get_auth_token(self):
        return self.__token

    def save_auth_token(self, user):
        user.log = "in"
        user.req_token = self.__token
        user.save()

    def is_authenticated(self):
        try:
            check_token = Authentications.objects.get(uid=self.token)
            return (check_token.user_id == self.__user_id)
        except:
            return False