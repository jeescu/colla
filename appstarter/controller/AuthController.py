from appstarter.models import User, Post, Authentication
from appstarter.services import AuthService, PasswordHelper
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
        pass_helper = PasswordHelper.PasswordHelper()

        now = timezone.localtime(timezone.now())

        if request.method == 'GET':

            try:
                # directing uri
                authentication = Authentication.objects.get(access_token=auth_service.get_token())
                auth_user = User.objects.get(pk=authentication.user_id)

                # active session
                # @TODO: Fix this
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
            user_name = request.POST['username']
            password = request.POST['password']

            try:

                if user_name != '' and password != '':
                    verified_user = User.objects.get(username=user_name)
                    auth_user = User.objects.get(pk=verified_user.id)

                    request_password = password
                    user_password = pass_helper.decode(verified_user.password)

                    if user_password == request_password:
                        auth_service.set_user(auth_user)
                        auth_service.add_session()
                        post = Post.objects.all().order_by('-date')[:10]
                        all_users = User.objects.order_by('username')

                        response.set_uri('colla/index.html')
                        response.set_data({'auth_user': auth_user, 'post': post, 'users': all_users})
                        return response.render(request)

                # returns error
                response.has_error()
                response.set_message('Wrong Username Password')
                return response.to_json()

            except Exception as e:
                print e
                response.has_error()
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
                    fullname=request.GET.get('first_name'),
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
            response.has_error()
            return response.to_json()

    def google_login(self, request):
        pass
