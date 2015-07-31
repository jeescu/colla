from appstarter.models import Chat, ChatUser, ChatMessage
from django.utils import timezone
from appstarter.utils import ResponseParcel

import json

class ChatController(object):
    
    def __init__(self):
        pass
    
    def get_message(self, request):
        response = ResponseParcel.ResponseParcel()
        sender = request.GET.get('sender')
        receiver = request.GET.get('reciever')
        
        sender_chat = ChatUser.objects.filter(user_id = sender)
        receiver_chat = ChatUser.objects.filter(user_id = receiver)
        
        messages = dict()
        
        # check if they had conversations
        if sender_chat.count() != 0 and receiver_chat.count() != 0:
            cnt_sender = 1

            for chat_from in sender_chat: 
                cnt_receiver = 1
                
                for chat_to in receiver_chat:
                    
                    if chat_from.chat_id == chat_to.chat_id:
                        
                        # They had conversation
                        chat_id = chat_from.chat_id
                        msg = ChatMessage.objects.filter(chat = chat_id).order_by('date_sent')
                        messages = self.prepare_message(msg)
                        break
                    
                    else:
                        
                        if sender_chat.count() == cnt_sender:

                            if receiver_chat.count() == cnt_receiver:

                                # They had no conversations
                                break
                            
                    cnt_receiver += 1
                    
                cnt_sender += 1

        response.set_data(messages)
        return response.data_to_json()
    
    def get_update_message(self, request):
        pass
    
    def new_message(self, request):
        response = ResponseParcel.ResponseParcel()
        sender = request.POST.get('sender')
        receiver = request.POST.get('reciever')
        message = request.POST.get('message')
        
        sender_chat = ChatUser.objects.filter(user_id=sender)
        receiver_chat = ChatUser.objects.filter(user_id=receiver)
        
        # check if they had conversations
        if sender_chat.count() != 0 and receiver_chat.count() != 0:
            cnt_sender = 1
            check_add = 0
            
            for chat_from in sender_chat:
                
                cnt_receiver = 1
                for chat_to in receiver_chat:
                    
                    if chat_from.chat_id == chat_to.chat_id:
                        
                        # They had conversation
                        chat_id = chat_from.chat_id
                        self.add_message(sender, message, chat_id)
                        check_add = 1
                        break
                    
                    else:
                        
                        if sender_chat.count() == cnt_sender:

                            if receiver_chat.count() == cnt_receiver and check_add == 0:

                                # They had no conversations
                                self.create_chat_conversation(sender, receiver, message)
                                check_add = 0
                                break
                            
                    cnt_receiver += 1
                    
                cnt_sender += 1

            response.set_message('Get Messages')
            return response.to_json()
        
        # Create new conversation to them
        else:
            self.create_chat_conversation(sender, receiver, message)
            response.set_message('get their new born chat')
            return response.to_json()

    def create_chat_conversation(self, sender, receiver, msg):
        users = [sender, receiver]
        
        chat = Chat(date_activated=timezone.now())
        chat.save()
        
        # add users to a chat
        for chat_user in users:
            chat.chatuser_set.create(
                user_id=chat_user
            )
        
        # add message their chat
        chat.chatmessage_set.create(
            user_id=sender,
            message=msg,
            date_sent=timezone.now()
        )
    
    def add_message(self, sender, msg, chat_id):
        chat = Chat.objects.get(pk=chat_id)
        
        # add message to their chat
        chat.chatmessage_set.create(
            user_id=sender,
            message=msg,
            date_sent=timezone.now()
        )
        
    def prepare_message(self, msg):
        messages = dict()
        count = 0
        
        for message in msg:
            count += 1
            messages[str(count)] = {
                "user_id": message.user_id,
                "message": message.message
            }
            messages['chat_id'] = message.chat_id
            
        return messages
