from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from appstarter.models import User, Authentication
from appstarter.controller import Auth


class UserController(object):
    
    def login(self, request):

        login = Auth.AuthController()
        return login.app_login(request)

    def register(self, request):
        
        return render(request, 'colla/signup.html', {})
        
    def do_register(self, request):

        try:
            new_user = User(
                username=request.POST['username'],
                password=request.POST['password']
            )

            new_user.save()
            new_user.profile_set.create(
                dis_name=request.POST['first_name'],
                profile_pic="/static/colla/images/profile_img/av-default.png",
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                middle_name=request.POST['middle_name'],
                position=request.POST['position'],
                company_name=request.POST['company'],
                mail_address=request.POST['mail']
            )
            return HttpResponse('Registered')
        
        except Exception as e:
            print e
            return HttpResponse('An error')   

    def logout(self, request):
        
        author_request = request.COOKIES   
        session_id = author_request.get('sessionid') or author_request.get('csrftoken')
        auth_user = Authentication.objects.get(access_token=session_id)
        auth_user.delete()
        
        return HttpResponseRedirect('/colla/', {})