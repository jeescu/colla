__author__ = 'john'

class ChatService(object):
    __chat_id = 0
    __user_id = 0

    def __init__(self, chat_id, user_id):
        self.__user_id = user_id
        self.__chat_id = chat_id

    def _messageValidated(self, message):
        return (len(message) <= 500)
