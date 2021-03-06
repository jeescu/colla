from appstarter.models import User, Profile, Post, Comment, Agree, ProfileImage, Authentication
from appstarter.forms import ImageUploadForm
from appstarter.utils import ResponseParcel
from appstarter import config
import os
    
class ProfileController(object):
    
    def __init__(self):
        pass
    
    def profile(self, request):
        response = ResponseParcel.ResponseParcel()
        
        try:
            auth = self.get_profile(request)
            user_profile = User.objects.get(pk=auth.user_id)

            response.set_uri('colla/profile.html')
            response.set_data({'user': user_profile})
            return response.render(request)
        
        except Exception as e:
            print e
            response.set_uri('/colla')
            return response.redirect()
        
    def get_profile(self, req):

        verify_request = req.COOKIES
        session_id = verify_request.get('sessionid') or verify_request.get('csrftoken')
        auth = Authentication.objects.get(access_token=session_id)
        return auth
    
    def update_profile(self, request):
        response = ResponseParcel.ResponseParcel()

        try:
            user_update = User.objects.get(pk=request.POST['user_id'])
            user_update.username = request.POST['username']
            user_update.save()

            form_image= ImageUploadForm(request.POST, request.FILES)

            profile_update = Profile.objects.get(user=user_update.id)

            if form_image.is_valid():
                
                img = ProfileImage(profile_image=form_image.cleaned_data['image'])
                img.save()

                try:
                    self.delete_profile_img(config.profile_update.profile_pic)
                    
                except:
                    pass

                profile_img_update = img.profile_image.url[config.env_img_concat_index:]
                profile_update.profile_pic = profile_img_update

            profile_update.dis_name = request.POST['display_name']
            profile_update.first_name = request.POST['first_name']
            profile_update.last_name = request.POST['last_name']
            profile_update.middle_name = request.POST['middle_name']
            profile_update.position = request.POST['position']
            profile_update.company_name = request.POST['company']
            profile_update.mail_address = request.POST['mail']
            
            profile_update.save()

            # update posts, comments, agrees
            post_update = Post.objects.filter(user=user_update.id)
            post_update.update(user_dis_name=profile_update.dis_name, user_pic=profile_update.profile_pic)

            for post in post_update:
                Comment.objects.filter(post=post.id).update(
                    user_name=profile_update.dis_name,
                    user_pic_url=profile_update.profile_pic
                )

                Agree.objects.filter(post=post.id).update(
                    user_name=profile_update.dis_name
                )

            return None
        
        except Exception as e:
            print e
            response.set_uri('/colla')
            return response.redirect()
    
    def delete_profile_img(self, img):
        
        if img != '/static/colla/images/profile_img/av-default.png':
            profile_dir = os.getcwd()+'/appstarter'
            os.remove(profile_dir+img)
