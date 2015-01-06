from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from appstarter.models import Question, Choice
from appstarter.models import User, Profile, Post, Comment, Group, GroupUser
from django.http import Http404
from django.views import generic
from django.utils import timezone

import json

class LoginView(generic.ListView):
    model = User
    template_name = 'colla/login.html'
    
    def get(self, request):
        verify_request = request.COOKIES
        try:
            # directing uri
            session_id = verify_request.get('sessionid') or verify_request.get('csrftoken')
            user_state = User.objects.get(req_token = session_id)
            # active session
            if user_state.log != 'out':
                
                user_profile = Profile.objects.get(user_id = user_state.id)
                post = Post.objects.all().order_by('-date')[:10]
                # comment = Comment.objects.all().order_by(post_id = post.id)
                return render(request,
                              'colla/index.html',
                              {'auth_user': user_state,'prof_user': user_profile, 'post':post})
        except:
            # log in
			return render(request, 'colla/login.html', {})
    
    def post(self, request, *args, **kwargs):
        authen_request = request.COOKIES
        try:
            auth_user = User.objects.get(username = request.POST['username'])
            if auth_user.password == request.POST['password']:
                auth_user.log = 'in'
                auth_user.req_token = authen_request.get('sessionid') or authen_request.get('csrftoken')
                auth_user.save()

                user_profile = Profile.objects.get(user_id = auth_user.id)
                post = Post.objects.all().order_by('-date')[:10]
                # comment = Comment.objects.all().order_by(post = post.id)
                return render(request,
                              'colla/index.html',
                              {'auth_user': auth_user,'prof_user': user_profile, 'post':post})
        except:
                return HttpResponse('Wrong Username Password')

        
class SignupView(generic.ListView):
    model = User
    template_name = 'colla/signup.html'

    
class HomeView(generic.ListView):
    model = User
    template_name = 'colla/index.html'
    context_object_name = 'auth_user'
    
    def get(self, request):
        return HttpResponseRedirect('/colla/', {})
    
    
class BaseController(object):
    # Get New Posts 5 secs interval
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

    def get_profile(self, request):
        pass

    def update_profile(self, request):
        pass
    
    # comment post
    def comment_post(self, request):
        post_id = request.GET.get('post_id')
        post_comment = Post.objects.get(pk=post_id)
        post_comment.comments = post_comment.comment + 1
        post_comment.comment_set.create (
            user_pic_url = request.GET.get('pic_url'),
            user_name = request.GET.get('user_name'),
            comment_date = timezone.now(),
            comment = request.GET.get('comment')
        )
        return HttpResponse(json.dumps({'status':'saved'}), content_type = "application/json")

    # agree post
    def agree_post(self, request):
        post_id = request.GET.get('post_id'),
        post_agree = Post.objects.get(pk=post_id)
        post_agree.agrees = post_agree.agrees + 1
        post_agree.save()
        post_agree.agree_set.create(
            user_name = request.GET.get('user_name')
        )
        return HttpResponse(json.dumps({'status':'saved'}), content_type = "application/json")
        
    # DONE
    def add_post(self, request):
        user_post = User.objects.get(pk=request.GET.get('userid'))
        user_post_profile = user_post.profile_set.get(user=user_post.id)
            
        user_post.post_set.create(
            user_pic = user_post_profile.profile_pic,
            user_dis_name = user_post_profile.dis_name,
            share_type = request.GET.get('sharetype'),
            title = request.GET.get('title') if request.GET.get('title') != "None" else "",
            content_text = request.GET.get('text'),
            content_image = request.GET.get('image') if request.GET.get('image') != "None" else "",
            content_link = request.GET.get('link') if request.GET.get('link') != "None" else "",
            date = timezone.now()
        )
        view_posts = {'status' : 'saved'}
        return HttpResponse(json.dumps(view_posts), content_type = "application/json")
    
    def add_issue(self, request):
        pass
    def add_message(self, request):
        pass
    
    # register
    def register(self, request):
        try:
            new_user = User(
                username = request.POST['username'],
                password = request.POST['password']
            )
            new_user.save()
            new_user.profile_set.create(
                dis_name = request.POST['first_name'],
                profile_pic = "/static/colla/images/profile_img/av-default.png",
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                middle_name = request.POST['middle_name'],
                position = request.POST['position'],
                company_name = request.POST['company'],
                mail_address = request.POST['mail']
            )
            return HttpResponse('Registered')
        except:    
            return HttpResponse('An error')   

    def logout(self, request):
        author_request = request.COOKIES   
        session_id = author_request.get('sessionid') or author_request.get('csrftoken')
        user_state = User.objects.get(req_token = session_id)
        user_state.log = 'out'
        user_state.req_token = ''
        user_state.save()
        return HttpResponseRedirect('/colla/', {})
    

class IndexView(generic.ListView):
    template_name = 'colla/question.html'
    context_object_name = 'latest_poll_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'colla/detail.html'
    context_object_name = 'poll'

    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'colla/results.html'
    context_object_name = 'poll'

def vote(request, poll_id):
    p = get_object_or_404(Question, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'colla/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('colla:results', args=(p.id,)))