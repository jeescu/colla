from appstarter.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views import generic
from django.utils import timezone
import json

class UserView(object):
    
    def __init__(self):
        pass
    
    def get_user(self, request):
        pass
    
    def login(self, request):
        pass
    
    def logout(self, request):
        pass
    
    def register(self, request):
        pass
    
    
class ProfileView(object):
    
    def __init__(self):
        pass
    
    def get_profile(self, request):
        verify_request = request.COOKIES
        session_id = verify_request.get('sessionid') or verify_request.get('csrftoken')
        user = User.objects.get(req_token = session_id)
        user_profile = User.objects.get(pk=user.id)
        return render(request, 'colla/profile.html', {'user': user_profile})
    
    def update_profile(self, request):
        try:
            user_profile_update = User.objects.get(pk=request.POST['id'])
            user_profile_update(
                username = request.POST['username']
            ).save()
            
            form_image= ImageUploadForm(request.POST, request.FILES)

            if form_image.is_valid():
                img = ProfileImage(profile_image=form.cleaned_data['image'])
                img.save()
                profile_img_update = img.profile_image.url[10:] 
                
            user_profile_update.profile_set.create(
                dis_name = request.POST['first_name'],
                profile_pic = profile_img_update,
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                middle_name = request.POST['middle_name'],
                position = request.POST['position'],
                company_name = request.POST['company'],
                mail_address = request.POST['mail']
            )
            return HttpResponse('Updated')
        except:    
            return HttpResponse('An error') 