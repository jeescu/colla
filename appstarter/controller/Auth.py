from appstarter.models import User, Authentications
from appstarter.service.AuthService import AuthService
from django.http import HttpResponse
from django.shortcuts import render
from appstarter.models import User, Post
    
class AuthController(object):
    
    def __init__(self):
        pass

    def app_login(self, request):

        if request.method == 'GET':
            verify_request = request.COOKIES
            try:
                # directing uri
                session_id = verify_request.get('sessionid') or verify_request.get('csrftoken')
                user_state = User.objects.get(req_token = session_id)
                auth_user = User.objects.get(pk=user_state.id)
                # active session
                if user_state.log != 'out':

                    post = Post.objects.all().order_by('-date')[:10]
                    all_users = User.objects.order_by('username')

                    return render(request,
                                  'colla/index.html',
                                  {'auth_user': auth_user, 'post':post, 'users':all_users })
            except:
                # log in
                return render(request, 'colla/login.html', {})

        if request.method == 'POST':

            authen_request = request.COOKIES
            try:
                ver_user = User.objects.get(username = request.POST['username'])
                auth_user = User.objects.get(pk=ver_user.id)

                print ver_user.password
                print request.POST['password']

                if ver_user.password == request.POST['password']:
                    ver_user.log = 'in'
                    print "tokening..."
                    ver_user.req_token = authen_request.get('sessionid') or authen_request.get('csrftoken')
                    ver_user.save()

                    post = Post.objects.all().order_by('-date')[:10]
                    all_users = User.objects.order_by('username')

                    return render(request,
                                  'colla/index.html',
                                  {'auth_user': auth_user, 'post':post, 'users':all_users})
                else:
                    return HttpResponse('Wrong Username Password')

            except Exception as e:
                print e
                return HttpResponse('Wrong Username Password')
        
    def facebook_login(self, request):
        session_id = request.GET.get('session')
        
        try:
            auth_user = Authentications.objects.get(uid=request.GET.get('id'))
            
            try:
                # app user
                user = User.objects.get(pk=auth_user.user_id)
                app_auth = AuthService(auth_user, session_id)
                app_auth.save_auth_token(user)
                # once user of the app is already connected to fb
                return
            
            except:
                # soc user
                soc_user = User.objects.get(sId=auth_user.uid)
                facebook_auth = AuthService(auth_user, session_id)
                facebook_auth.save_auth_token(soc_user)
                return
            
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
                profile_pic = 'http://graph.facebook.com/'+request.GET.get('id')+'/picture?type=large'
            )

            return HttpResponse('')

    def google_login(self, request):
        pass