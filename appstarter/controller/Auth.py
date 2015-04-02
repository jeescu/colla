from appstarter.models import User, Authentications
from appstarter.service.AuthService import AuthService
from django.http import HttpResponse

    
class AuthController(object):
    
    def __init__(self):
        pass

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