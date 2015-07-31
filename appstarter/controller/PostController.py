from django.http import HttpResponse, HttpResponseRedirect
from appstarter.models import User, Post, PostImage
from appstarter.forms import ImageUploadForm
from django.utils import timezone
from appstarter.utils import ResponseParcel


class PostController(object):

    def __init__(self):
        pass
    
    def get_new_post(self, request):
        response = ResponseParcel.ResponseParcel()
        post_update = dict()

        if request.GET.get('latest') == "None":
            
            try:
                # Get fresh post
                post = Post.objects.all().order_by('-date')[:10]
                post_update = self.prepare_new_post(post)
            
            except:
                # No posts
                post_update['status'] = 'Unavailable'
                
        else:
            get_client_latest_post = int(request.GET.get('latest'))
            check_post = Post.objects.all().order_by('-date').first()
            
            # check if there is a post update
            if check_post.id == get_client_latest_post:
                # posts are already updated
                post_update['status'] = 'updated'
                pass
            else:
                get_update = Post.objects.all().order_by('-date')
               
                post_update = self.get_update_post(get_update, get_client_latest_post)

        response.set_data(post_update)
        return response.data_to_json()
    
    def prepare_new_post(self, all_post):
        post = dict()
        count = 0
        
        for posts in all_post:
            count += 1
            
            commented = dict()
            agreed = dict()
            
            com_count = 1
            
            for comment in posts.comment():
                commented[com_count] = {
                    "user_pic_url": comment.user_pic_url,
                    "user_name": comment.user_name,
                    "comment_date": comment.comment_date.strftime('%b. %d, %G, %I:%M %p'),
                    "comment": comment.comment
                }
                
                com_count += 1
            
            agree_count = 1
            
            for agree in posts.agreed():
                agreed[agree_count] = {
                    'user_name': agree.user_name
                }
                
                agree_count += 1
                
            post['post'+str(count)] = {
                "post_id": posts.id,
                "pic": posts.user_pic,
                "display_name": posts.user_dis_name,
                "share": posts.share_type,
                "date": str(posts.date),
                "title": posts.title,
                "text": posts.content_text,
                "image": posts.content_image,
                "link": posts.content_link,
                "agrees": posts.agrees,
                "comments": posts.comments,
                "commented": commented,
                "agreed": agreed
            }
            
        return post
    
    def get_update_post(self, all_post, latest_post):
        post = dict()
        count = 0
                
        for posts in all_post:
            count += 1
            
            if posts.id != latest_post:
                post['post'+str(count)] = {
                    "post_id": posts.id,
                    "pic": posts.user_pic,
                    "display_name": posts.user_dis_name,
                    "share": posts.share_type,
                    "date": str(posts.date),
                    "title": posts.title,
                    "text": posts.content_text,
                    "image": posts.content_image,
                    "link": posts.content_link,
                    "agrees": posts.agrees,
                    "comments": posts.comments
                }
                
            else:
                break
        
        return post
    
    def get_more_post(self, request):
        response = ResponseParcel.ResponseParcel()
        post_offset = request.GET.get('offset')
        offset = int(post_offset)
        
        try:
            more_post = Post.objects.all().order_by('-date')[offset:offset+10]
            posts = self.prepare_new_post(more_post)
            
        except Exception as e:
            print e
            posts = {'status': 'no more post'}

        response.set_data(posts)
        return response.data_to_json()
        
    def search(self, request):
        pass
    
    def comment_post(self, request):
        response = ResponseParcel.ResponseParcel()
        try:
            post_id = request.POST.get('post_id')
            post_comment = Post.objects.get(pk=post_id)
            post_comment.comments += 1
            post_comment.save()
            post_comment.comment_set.create(
                user_pic_url=request.POST.get('pic'),
                user_name=request.POST.get('user_name'),
                comment_date=timezone.now(),
                comment=request.POST.get('comment')
            )
            response.set_data({'status': 'comment saved'})
            return response.data_to_json()
        
        except Exception as e:
            print e
            response.set_uri('/colla')
            return response.redirect()

    def agree_post(self, request):
        response = ResponseParcel.ResponseParcel()
        try:
            post_id = request.POST.get('post_id')
            post_name_agreed = request.POST.get('user_name')
            post_agree = Post.objects.get(pk=post_id)

            # Checks only anybody who agreed
            if post_agree.user_dis_name != post_name_agreed:
                user_agreed = "Nobody"
                post_agree_checked = post_agree.agree_set.filter(user_name=post_name_agreed)
                
                for post in post_agree_checked:
                    user_agreed = post.user_name

                if user_agreed == post_name_agreed:
                    response.set_data({'status': 'Already agreed'})
                    return response.data_to_json()

                else:
                    post_agree.agrees += 1
                    post_agree.save()
                    post_agree.agree_set.create(
                        user_name=post_name_agreed
                    )
                    response.set_data({'status': 'agreed'})
                    return response.data_to_json()

            else:
                response.set_data({'status': 'You owned the post'})
                return response.data_to_json()

        except Exception as e:
            print e
            response.set_uri('/colla')
            return response.redirect()

    # @TODO: Please resolve this
    def add_post(self, request):
        response = ResponseParcel.ResponseParcel()
        try:
            post_img = ""
            image_data = ImageUploadForm(request.POST, request.FILES)

            if image_data.is_valid():

                img = PostImage(post_image=image_data.cleaned_data['image'])
                img.save()
                post_img = img.post_image.url[10:]
                # prod
                # post_img = img.post_image.url[21:]

            user_post = User.objects.get(pk=request.POST.get('userid'))
            user_post_profile = user_post.profile_set.get(user=user_post.id)

            user_post.post_set.create(
                user_pic=user_post_profile.profile_pic,
                user_dis_name=user_post_profile.dis_name,
                share_type=request.POST.get('share'),
                title=request.POST.get('title') if request.POST.get('title') != "None" else "",
                content_text=request.POST.get('text'),
                content_image=post_img,
                content_link=request.POST.get('link') if request.POST.get('link') != "None" else "",
                date=timezone.now()
            )

            response.set_data({'status': 'saved', 'image': post_img})
            return response.data_to_json()
        
        except Exception as e:
            print e
            response.set_data({'status': 'error'})
            return response.data_to_json()
    
    def add_issue(self, request):
        pass
    
    def add_message(self, request):
        pass
