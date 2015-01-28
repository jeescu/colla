from appstarter.models import User, Profile, Authentications
from appstarter.forms import ImageUploadForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views import generic
from django.utils import timezone
import os

import json

    
class socialLogin(object):
    
    def __init__(self):
        pass
    
    def facebook_login(self, request):
        session_id = request.GET.get('session')
        
        try:
            auth_user = Authentications.objects.get(uid = request.GET.get('id'))
            
            try:
                # app user
                user = User.objects.get(pk = auth_user.user_id)
                self.onLogin(user, session_id)
                # once user of the app is already connected to fb
                return
            
            except:
                # soc user
                soc_user = User.objects.get(sId = auth_user.uid)
                self.onLogin(soc_user, session_id)
                
                return HttpResponse('')
            
        except:
            # new soc user
            new_auth_user = Authentications(
                uid = request.GET.get('id'),
                provider = request.GET.get('provider'),
                access_token = request.GET.get('accessToken')
            )

            new_auth_user.save()

            new_social_user = User(
                sId = request.GET.get('id'),
                log = 'in',
                req_token = session_id
            )

            new_social_user.save()

            new_social_user.profile_set.create(
                dis_name = request.GET.get('name'),
                first_name = request.GET.get('first_name'),
                last_name = request.GET.get('last_name'),
                profile_pic = 'http://graph.facebook.com/'+request.GET.get('id')+'/picture'
            )

            return HttpResponse('')
    
    def google_login(self, request):
        pass
    
    def onLogin(self, user, session):
        user.log = 'in'
        user.req_token = session
        user.save()