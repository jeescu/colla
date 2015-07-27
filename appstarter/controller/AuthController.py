from appstarter import config
from django.http import HttpResponse
from django.shortcuts import render
from appstarter.models import User, Post, Authentication
from appstarter.service import AuthService
from datetime import timedelta
from django.utils import timezone

# @TODO: Please move auth logic to authService
class AuthController(object):
    
    def __init__(self):
        pass

    def app_login(self, request):
        app_config = config
        now = timezone.localtime(timezone.now())

        if request.method == 'GET':
            verify_request = request.COOKIES
            try:
                # directing uri
                session_id = verify_request.get('sessionid') or verify_request.get('csrftoken')
                authentication = Authentication.objects.get(access_token=session_id)
                auth_user = User.objects.get(pk=authentication.user_id)
                # active session
                print authentication.expired_at
                print now

                if authentication.expired_at > now:
                    post = Post.objects.all().order_by('-date')[:10]
                    all_users = User.objects.order_by('username')

                    return render(request, 'colla/index.html',
                                  {'auth_user': auth_user, 'post': post, 'users': all_users})

                else:
                    auth_service = AuthService.AuthService()
                    auth_service.end_session(request)
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
                        expired_at=now+timedelta(hours=app_config.expires)
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
        app_config = config
        now = timezone.localtime(timezone.now())

        request_cookie = request.COOKIES
        session_token = request_cookie.get('sessionid') or request_cookie.get('csrftoken')
        
        try:

            try:
                Authentication.objects.get(provider_user_id=request.GET.get('id'))

            except Exception as e:
                print "new social user"
                # new soc user
                new_social_user = User(
                    user_fullname=request.GET.get('first_name')
                )

                new_social_user.save()

                new_social_user.profile_set.create(
                    dis_name=request.GET.get('name'),
                    first_name=request.GET.get('first_name'),
                    last_name=request.GET.get('last_name'),
                    profile_pic='http://graph.facebook.com/'+request.GET.get('id')+'/picture?type=large'
                )

                new_auth_user = Authentication(
                    user_id=new_social_user.id,
                    provider=request.GET.get('provider'),
                    provider_user_id=request.GET.get('id'),
                    access_token=session_token,
                    expired_at=now + timedelta(hours=app_config.expires)
                )

                new_auth_user.save()

                return HttpResponse('')

        except Exception as e:
            print e
            return

    def google_login(self, request):
        pass
