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

    def save_auth_token(self, new_auth):
        new_auth.log = "in"
        new_auth.req_token = self.__token
        new_auth.save()


    def authenticated(self):
        try:
            check_token = Authentications.objects.get(uid=self.token)
            return (check_token.user_id == self.__user_id)
        except:
            return False