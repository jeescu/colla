from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from appstarter.models import User, Profile, Post, Comment, Group, GroupUser, PostImage
from appstarter.forms import ImageUploadForm
from django.http import Http404
from django.views import generic
from django.utils import timezone

import json

class activityController(generic.ListView):
    model = User
    template_name = 'colla/index.html'
    context_object_name = 'auth_user'
    
    def __init__(self):
        pass
    
    def get(self, request):
        return HttpResponseRedirect('/colla/', {})
    
    def get_new_post(self, request):
        post_update = dict()

        if request.GET.get('latest') == "None":
            try:
                count = 0
                # Get Post if Someone added
                post = Post.objects.all().order_by('-date')[:10]
                for posts in post:
                    count=count + 1
                    post_update['post'+str(count)] = {
                        "post_id" : posts.id,
                        "pic" : posts.user_pic,
                        "display_name" : posts.user_dis_name,
                        "share" : posts.share_type, 
                        "date" : str(posts.date),
                        "title" : posts.title,
                        "text" : posts.content_text,
                        "image" : posts.content_image,
                        "link" : posts.content_link,
                        "agrees" : posts.agrees,
                        "comments" : posts.comments
                    }
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
                count = 0
                get_update_post = Post.objects.all().order_by('-date')
                
                for posts in get_update_post:
                    count=count + 1
                    if posts.id !=  get_client_latest_post:
                        post_update['post'+str(count)] = {
                            "post_id" : posts.id,
                            "pic" : posts.user_pic,
                            "display_name" : posts.user_dis_name,
                            "share" : posts.share_type, 
                            "date" : str(posts.date),
                            "title" : posts.title,
                            "text" : posts.content_text,
                            "image" : posts.content_image,
                            "link" : posts.content_link,
                            "agrees" : posts.agrees,
                            "comments" : posts.comments
                        }
                    else:
                        break
        return HttpResponse(json.dumps(post_update), content_type = "application/json")
    
    # menu action
    def search(self, request):
        pass
    
    # comment post
    def add_comment(self, request):
        post_id = request.POST.get('post_id')
        post_comment = Post.objects.get(pk=post_id)
        post_comment.comments = post_comment.comments + 1
        post_comment.save()
        post_comment.comment_set.create (
            user_pic_url = request.POST.get('pic'),
            user_name = request.POST.get('user_name'),
            comment_date = timezone.now(),
            comment = request.POST.get('comment')
        )
        return HttpResponse(json.dumps({'status':'comment saved'}), content_type = "application/json")

    # agree post
    def agree_post(self, request):
        post_id = request.POST.get('post_id')
        post_name_agreed = request.POST.get('user_name')
        post_agree = Post.objects.get(pk=post_id)
        
        # Checks only anybody who agreed
        if  post_agree.user_dis_name != post_name_agreed:
            user_agreed = "Nobody"
            post_agree_checked = post_agree.agree_set.filter(user_name = post_name_agreed)
            for post in post_agree_checked:
                user_agreed = post.user_name
                
            if user_agreed == post_name_agreed:
                data = {'status': 'Already agreed'}
                return HttpResponse(json.dumps(data),
                                content_type = "application/json")
            else:
                post_agree.agrees = post_agree.agrees + 1
                post_agree.save()
                post_agree.agree_set.create(
                    user_name = post_name_agreed
                )
                data = {'status': 'agreed'}
                return HttpResponse(json.dumps(data),
                                    content_type = "application/json")
        else:
            data = {'status':'You owned the post'}
            return HttpResponse(json.dumps(data),
                                content_type = "application/json")
        
    # DONE
    def add_post(self, request):

        if request.method == 'POST':

            post_img = ""
            form = ImageUploadForm(request.POST, request.FILES)

            if form.is_valid():

                img = PostImage(post_image=form.cleaned_data['image'])
                img.save()
                post_img = img.post_image.url[10:]

            user_post = User.objects.get(pk=request.POST.get('userid'))
            user_post_profile = user_post.profile_set.get(user=user_post.id)
                
            user_post.post_set.create(
                user_pic = user_post_profile.profile_pic,
                user_dis_name = user_post_profile.dis_name,
                share_type = request.POST.get('share'),
                title = request.POST.get('title') if request.POST.get('title') != "None" else "",
                content_text = request.POST.get('text'),
                content_image = post_img,
                content_link = request.POST.get('link') if request.POST.get('link') != "None" else "",
                date = timezone.now()
            )

            view_posts = {'status' : 'saved'}

            return HttpResponse(json.dumps(view_posts), content_type = "application/json")
    
    def add_issue(self, request):
        pass
    
    def add_message(self, request):
        pass

