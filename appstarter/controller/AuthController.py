from django.shortcuts import render
from appstarter.models import User, Post, Authentication
from appstarter.services import AuthService
from django.utils import timezone
from appstarter.utils import ResponseParcel


# @TODO: Please move auth logic to authService
class AuthController(object):
    
    def __init__(self):
        pass

    def app_login(self, request):
        response = ResponseParcel.ResponseParcel()
        auth_service = AuthService.AuthService()
        auth_service.set_request_data(request)
        now = timezone.localtime(timezone.now())

        if request.method == 'GET':
            verify_request = request.COOKIES
            try:
                # directing uri
                authentication = Authentication.objects.get(access_token=auth_service.get_token())
                auth_user = User.objects.get(pk=authentication.user_id)

                # active session
                if authentication.expired_at > now:
                    post = Post.objects.all().order_by('-date')[:10]
                    all_users = User.objects.order_by('username')

                    response.set_data({'auth_user': auth_user, 'post': post, 'users': all_users})
                    response.set_uri('colla/index.html')
                    return response.render(request)

                else:
                    auth_service.end_session()
                    raise Exception("Expired token")

            except Exception as e:
                print e
                response.set_uri('colla/login.html')
                return response.render(request)

        if request.method == 'POST':
            try:
                verified_user = User.objects.get(username=request.POST['username'])
                auth_user = User.objects.get(pk=verified_user.id)

                if verified_user.password == request.POST['password']:
                    auth_service.set_user(auth_user)
                    auth_service.add_session()

                    post = Post.objects.all().order_by('-date')[:10]
                    all_users = User.objects.order_by('username')

                    response.set_uri('colla/index.html')
                    response.set_data({'auth_user': auth_user, 'post': post, 'users': all_users})
                    return response.render(request)

                else:
                    response.error()
                    response.set_message('Wrong Username Password')
                    return response.to_json()

            except Exception as e:
                print e
                response.error()
                response.set_message('Wrong Username Password')
                return response.to_json()
        
    def facebook_login(self, request):
        response = ResponseParcel.ResponseParcel()
        auth_service = AuthService.AuthService()
        
        try:

            try:
                social_user = User.objects.get(provider_user_id=request.GET.get('id'))

            except Exception as e:
                print "new social user"
                # new soc user
                social_user = User(
                    user_fullname=request.GET.get('first_name'),
                    provider_user_id=request.GET.get('id')
                )

                social_user.save()

                social_user.profile_set.create(
                    dis_name=request.GET.get('name'),
                    first_name=request.GET.get('first_name'),
                    last_name=request.GET.get('last_name'),
                    profile_pic='http://graph.facebook.com/'+request.GET.get('id')+'/picture?type=large'
                )

            auth_service.set_request_data(request)
            auth_service.set_user(social_user)
            auth_service.add_session()

            response.set_message('Success')
            return response.to_json()

        except Exception as e:
            print e
            response.error()
            return response.to_json()

    def google_login(self, request):
        pass
