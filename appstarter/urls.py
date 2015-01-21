from django.conf.urls import patterns, url
from appstarter.controller import Base, Activity, Issue, Monitor, Project, Monitor, User

urlpatterns = patterns('',
    url(r'^$', Base.LoginView.as_view(), name='login'),                
    url(r'^signup/$', Base.SignupView.as_view(), name='signup'),
                    
    url(r'^dashboard/$', Activity.activityController.as_view(), name='home'),           
    url(r'^new-post/$', Activity.activityController().add_post, name='new_post'),
    url(r'^new-comment/$', Activity.activityController().add_comment, name='new_comment'),
    url(r'^new-agree/$', Activity.activityController().agree_post, name='agree_post'),
    url(r'^update-post/$', Activity.activityController().get_new_post, name='update_post'),
    
    url(r'^profile/$', User.ProfileView().profile, name='profile'),
    url(r'^profile/update-profile/$', User.ProfileView().update_profile, name='update_profile'),
    url(r'^register/', Base.BaseController().register, name='register'), 
    url(r'^logout', Base.BaseController().logout, name='logout'), 
)