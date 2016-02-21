__author__ = 'john'

from appstarter.models import User, PostImage, Article
from appstarter.forms import ImageUploadForm
from django.utils import timezone
from appstarter.utils import ResponseParcel
from appstarter import config


class ArticleController(object):

    def __init__(self):
        pass

    def browse(self, request):
        response = ResponseParcel.ResponseParcel()
        articles = dict()

        try:
            article = Article.objects.all().order_by('-date')
            articles = self.prepare(article)

        except Exception as e:
            print e

        response.set_data(articles)
        return response.data_to_json()

    def read(self, request):
        pass

    # @FIXME: please resolve this
    def create(self, request):
        response = ResponseParcel.ResponseParcel()
        try:
            cover_img = ""
            image_data = ImageUploadForm(request.POST, request.FILES)

            if image_data.is_valid():

                img = PostImage(post_image=image_data.cleaned_data['image'])
                img.save()
                cover_img = img.post_image.url[config.env_img_concat_index:]

            user = User.objects.get(pk=request.POST.get('userId'))

            user.article_set.create(
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

    def prepare(self, all_articles):
        articles = dict()
        count = 0

        for article in all_articles:
            count += 1

            articles['article'+str(count)] = {
                'pic': article.user.profile().profile_pic,
                'display_name': article.user.profile().dis_name,
                'title': article.title,
                'content': article.content,
                'cover': article.cover,
                'date': str(article.date)
            }

        return articles