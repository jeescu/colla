from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from appstarter.models import Question, Choice
from appstarter.models import User, Profile
from django.http import Http404
from django.views import generic

# Create your views here.

class LoginView(generic.ListView):
    model = User
    template_name = 'colla/login.html'
    
class SignupView(generic.ListView):
    model = User
    template_name = 'colla/signup.html'
    
class HomeView(generic.ListView):
    model = User
    template_name = 'colla/index.html'

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