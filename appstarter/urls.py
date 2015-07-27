from django.conf.urls import patterns, url
from appstarter.controller import UserController, PostController, ProfileController, AuthController, ChatController

urlpatterns = patterns('',
    
    # Login and Signup
    url(r'^$', UserController.UserController().login, name='login'),
    url(r'^signup/$', UserController.UserController().register, name='signup'),
    url(r'^register/', UserController.UserController().do_register, name='register'),
    
    # Authentications
    url(r'^login/facebook/$', AuthController.AuthController().facebook_login, name='facebook_login'),
    url(r'^login/google/$', AuthController.AuthController().google_login, name='google_login'),
                       
    # Home and Post                   
    url(r'^dashboard/$', PostController.PostController().get, name='home'),
    url(r'^new-post/$', PostController.PostController().add_post, name='new_post'),
    url(r'^update-post/$', PostController.PostController().get_new_post, name='update_post'),
    url(r'^more-post/$', PostController.PostController().get_more_post, name='more_post'),
                     
    # Agree and Comment                   
    url(r'^new-comment/$', PostController.PostController().comment_post, name='new_comment'),
    url(r'^new-agree/$', PostController.PostController().agree_post, name='agree_post'),
    
    # Chat                   
    url(r'^new-message/$', ChatController.ChatController().new_message, name='new_message'),
    url(r'^get-messages/$', ChatController.ChatController().get_message, name='get_message'),
    url(r'^get-update-messages/$', ChatController.ChatController().get_update_message, name='get_update_message'),
    
    # Profile
    url(r'^profile/$', ProfileController.ProfileController().profile, name='profile'),
    url(r'^profile/update-profile/$', ProfileController.ProfileController().update_profile, name='update_profile'),
    
    url(r'^logout', UserController.UserController().logout, name='logout'),
)