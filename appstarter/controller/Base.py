from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from appstarter.models import User, Profile, Post, Comment, Group, GroupUser
from appstarter.models import PostImage
from appstarter.forms import ImageUploadForm
from django.http import Http404
from django.views import generic
from django.utils import timezone

import json

class LoginView(generic.ListView):
    model = User
    template_name = 'colla/login.html'
    
    def get(self, request):
        verify_request = request.COOKIES
        try:
            # directing uri
            session_id = verify_request.get('sessionid') or verify_request.get('csrftoken')
            user_state = User.objects.get(req_token = session_id)
            auth_user = User.objects.get(pk=user_state.id)
            # active session
            if user_state.log != 'out':
                
                post = Post.objects.all().order_by('-date')[:10]

                return render(request, 
                              'colla/index.html',
                              {'auth_user': auth_user, 'post':post})
        except:
            # log in
			return render(request, 'colla/login.html', {})
    
    def post(self, request, *args, **kwargs):
        authen_request = request.COOKIES
        try:
            ver_user = User.objects.get(username = request.POST['username'])
            auth_user = User.objects.get(pk=ver_user.id)
            if ver_user.password == request.POST['password']:
                ver_user.log = 'in'
                ver_user.req_token = authen_request.get('sessionid') or authen_request.get('csrftoken')
                ver_user.save()

                post = Post.objects.all().order_by('-date')[:10]

                return render(request,
                              'colla/index.html',
                              {'auth_user': auth_user, 'post':post})
            else:
                return HttpResponse('Wrong Username Password')
            
        except:
            return HttpResponse('Wrong Username Password')

        
class SignupView(generic.ListView):
    model = User
    template_name = 'colla/signup.html'
    
    
class BaseController(object):
    # register
    def register(self, request):
        try:
            new_user = User(
                username = request.POST['username'],
                password = request.POST['password']
            )
            new_user.save()
            new_user.profile_set.create(
                dis_name = request.POST['first_name'],
                profile_pic = "/static/colla/images/profile_img/av-default.png",
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                middle_name = request.POST['middle_name'],
                position = request.POST['position'],
                company_name = request.POST['company'],
                mail_address = request.POST['mail']
            )
            return HttpResponse('Registered')
        except:    
            return HttpResponse('An error')   

    def logout(self, request):
        author_request = request.COOKIES   
        session_id = author_request.get('sessionid') or author_request.get('csrftoken')
        user_state = User.objects.get(req_token = session_id)
        user_state.log = 'out'
        user_state.req_token = ''
        user_state.save()
        return HttpResponseRedirect('/colla/', {})