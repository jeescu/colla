from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from appstarter.models import Question, Choice
from appstarter.models import User, Profile
from django.http import Http404
from django.views import generic
from django.contrib.auth import logout


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
                return render(request, 'colla/index.html', {'auth_user': user_state})
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
                return render(request, 'colla/index.html', {'auth_user': auth_user})
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
    
    # menu action
    def search(self, request):
        pass
    def get_profile(self, request):
        pass
    
    # comment post
    def comment_post(self, request):
        pass
        
    # agree post
    def agree_post(self, request):
        pass
        
    # new activity
    def add_post(self, request):
        pass
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