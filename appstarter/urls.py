from django.conf.urls import patterns, url
from appstarter.controller import views

urlpatterns = patterns('',
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^logout', views.BaseController().logout, name='logout'),                 
    url(r'^dashboard/$', views.HomeView.as_view(), name='home'),
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^question/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)