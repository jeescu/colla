from appstarter.models import Authentication
from django.http import HttpResponse
from django.shortcuts import render
from appstarter.models import User, Post
import datetime

# @TODO: Please move auth logic to authService
class AuthController(object):
    
    def __init__(self):
        pass

    def app_login(self, request):

        if request.method == 'GET':
            verify_request = request.COOKIES
            try:
                # directing uri
                session_id = verify_request.get('sessionid') or verify_request.get('csrftoken')
                authentication = Authentication.objects.get(access_token=session_id)
                auth_user = User.objects.get(pk=authentication.user_id)
                # active session
                if authentication.expires < datetime.datetime.now():
                    post = Post.objects.all().order_by('-date')[:10]
                    all_users = User.objects.order_by('username')

                    return render(request, 'colla/index.html',
                                  {'auth_user': auth_user, 'post': post, 'users': all_users})

                else:
                    raise Exception("Expired token")

            except Exception as e:
                # log in
                print e
                return render(request, 'colla/login.html', {})

        if request.method == 'POST':

            request_cookie = request.COOKIES
            try:
                verified_user = User.objects.get(username=request.POST['username'])
                auth_user = User.objects.get(pk=verified_user.id)

                if verified_user.password == request.POST['password']:
                    session_token = request_cookie.get('sessionid') or request_cookie.get('csrftoken')

                    authenticated_user = Authentication(
                        user_id=verified_user.id,
                        access_token=session_token,
                        expired_at=datetime.datetime.now()
                    )
                    authenticated_user.save()

                    post = Post.objects.all().order_by('-date')[:10]
                    all_users = User.objects.order_by('username')

                    return render(request, 'colla/index.html',
                                  {'auth_user': auth_user, 'post': post, 'users': all_users})
                else:
                    return HttpResponse('Wrong Username Password')

            except Exception as e:
                print e
                return HttpResponse('Wrong Username Password')
        
    def facebook_login(self, request):

        request_cookie = request.COOKIES
        session_token = request_cookie.get('sessionid') or request_cookie.get('csrftoken')
        
        try:
            auth_user = Authentication.objects.get(provider_user_id=request.GET.get('id'))

            if auth_user is not None:
                return

            else:
                # new soc user
                new_auth_user = Authentication(
                    provider=request.GET.get('provider'),
                    provider_user_id=request.GET.get('id'),
                    access_token=session_token,
                    expired_at=datetime.datetime.now()
                )

                new_auth_user.save()

                new_social_user = User()
                new_social_user.profile_set.create(
                    dis_name=request.GET.get('name'),
                    first_name=request.GET.get('first_name'),
                    last_name=request.GET.get('last_name'),
                    profile_pic='http://graph.facebook.com/'+request.GET.get('id')+'/picture?type=large'
                )

                return HttpResponse('')

        except Exception as e:
            print e
            return

    def google_login(self, request):
        pass
