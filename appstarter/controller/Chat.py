from appstarter.models import User, Profile, Post, Chat, ChatUser, ChatMessage
from appstarter.forms import ImageUploadForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views import generic
from django.utils import timezone
import os

import json

class ChatController(object):
    
    def __init__(self):
        pass
    
    def get_message(self, request):
        sender = request.GET.get('sender')
        reciever = request.GET.get('reciever')
        
        sender_chat = ChatUser.objects.filter(user_id = sender)
        reciever_chat = ChatUser.objects.filter(user_id = reciever)
        
        messages = dict()
        
        # check if they had conversations
        if sender_chat.count() != 0 and reciever_chat.count() != 0:
            cnt_sender = 1

            for chat_from in sender_chat:
                
                cnt_reciever = 1
                for chat_to in reciever_chat:
                    
                    if chat_from.chat_id == chat_to.chat_id:
                        
                        # They had conversation
                        chat_id = chat_from.chat_id
                        msg = ChatMessage.objects.filter(chat = chat_id).order_by('date_sent')
                        messages = self.prepare_message(msg)
                        break
                    
                    else:
                        
                        if sender_chat.count() == cnt_sender:

                            if reciever_chat.count() == cnt_reciever:

                                # They had no conversations
                                break
                            
                    cnt_reciever += 1
                    
                cnt_sender += 1
                
        return HttpResponse(json.dumps(messages), content_type = "application/json")
    
    def get_update_message(self, request):
        pass
    
    def new_message(self, request):
        sender = request.POST.get('sender')
        reciever = request.POST.get('reciever')
        message = request.POST.get('message')
        
        sender_chat = ChatUser.objects.filter(user_id = sender)
        reciever_chat = ChatUser.objects.filter(user_id = reciever)
        
        # check if they had conversations
        if sender_chat.count() != 0 and reciever_chat.count() != 0:
            cnt_sender = 1
            check_add = 0
            
            for chat_from in sender_chat:
                
                cnt_reciever = 1
                for chat_to in reciever_chat:
                    
                    if chat_from.chat_id == chat_to.chat_id:
                        
                        # They had conversation
                        chat_id = chat_from.chat_id
                        self.add_message(sender, message, chat_id)
                        check_add = 1
                        break
                    
                    else:
                        
                        if sender_chat.count() == cnt_sender:

                            if reciever_chat.count() == cnt_reciever and check_add == 0:

                                # They had no conversations
                                self.create_chat_conversation(sender, reciever, message)
                                check_add = 0
                                break
                            
                    cnt_reciever += 1
                    
                cnt_sender += 1
                
            return HttpResponse('get their message')
        
        # Create new conversation to them
        else:
            self.create_chat_conversation(sender, reciever, message)
            return HttpResponse('get their new born chat')  
#            return HttpResponse(json.dumps({'status': sender_chat.count()}), content_type = "application/json")
    
    
    def create_chat_conversation(self, sender, reciever, msg):
        users = [sender, reciever]
        
        chat = Chat(date_activated = timezone.now())
        chat.save()
        
        # add users to a chat
        for chat_user in users:
            chat.chatuser_set.create(
                user_id = chat_user
            )
        
        # add message their chat
        chat.chatmessage_set.create(
            user_id = sender,
            message = msg,
            date_sent = timezone.now()
        )
    
    def add_message(self, sender, msg, chat_id):
        chat = Chat.objects.get(pk = chat_id)
        
        # add message to their chat
        chat.chatmessage_set.create(
            user_id = sender,
            message = msg,
            date_sent = timezone.now()
        )
        
    def prepare_message(self, msg):
        messages = dict()
        count = 0
        
        for message in msg:
            count=count + 1
            messages[str(count)] = {
                "user_id" : message.user_id,
                "message" : message.message
            }
            messages['chat_id'] = message.chat_id
            
        return messages