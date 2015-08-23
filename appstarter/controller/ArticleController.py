__author__ = 'john'

from appstarter.models import User, PostImage
from appstarter.forms import ImageUploadForm
from django.utils import timezone
from appstarter.utils import ResponseParcel


class ArticleController(object):

    def __init__(self):
        pass

    def create(self, request):
        response = ResponseParcel.ResponseParcel()
        try:
            cover_img = ""
            image_data = ImageUploadForm(request.POST, request.FILES)

            if image_data.is_valid():

                img = PostImage(post_image=image_data.cleaned_data['image'])
                img.save()
                cover_img = img.post_image.url[10:]
                # prod
                # post_img = img.post_image.url[21:]

            user = User.objects.get(pk=request.POST.get('userId'))
            user_profile = user.profile_set.get(user=user.id)

            user.article_set.create(
                user_pic=user_profile.profile_pic,
                user_dis_name=user_profile.dis_name,
                title=request.POST.get('title') if request.POST.get('title') != "None" else "",
                content=request.POST.get('content'),
                cover=cover_img,
                date=timezone.now()
            )

            response.set_data({'status': 'saved', 'image': cover_img})
            return response.data_to_json()

        except Exception as e:
            print e
            response.set_data({'status': 'error'})
            return response.data_to_json()

    def update(self, request):
        pass

    def remove(self, request):
        pass