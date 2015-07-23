from django.conf.urls import patterns, url
from appstarter.controller import User, Post, Profile, Auth, Chat

urlpatterns = patterns('',
    
    # Login and Signup
    url(r'^$', User.UserController().login, name='login'),                
    url(r'^signup/$', User.UserController().register, name='signup'),
    url(r'^register/', User.UserController().do_register, name='register'),
    
    # Authentications
    url(r'^login/facebook/$', Auth.AuthController().facebook_login, name='facebook_login'),
    url(r'^login/google/$', Auth.AuthController().google_login, name='google_login'),
                       
    # Home and Post                   
    url(r'^dashboard/$', Post.PostController().get, name='home'),           
    url(r'^new-post/$', Post.PostController().add_post, name='new_post'),
    url(r'^update-post/$', Post.PostController().get_new_post, name='update_post'),
    url(r'^more-post/$', Post.PostController().get_more_post, name='more_post'),
                     
    # Agree and Comment                   
    url(r'^new-comment/$', Post.PostController().comment_post, name='new_comment'),
    url(r'^new-agree/$', Post.PostController().agree_post, name='agree_post'),
    
    # Chat                   
    url(r'^new-message/$', Chat.ChatController().new_message, name='new_message'),
    url(r'^get-messages/$', Chat.ChatController().get_message, name='get_message'),
    url(r'^get-update-messages/$', Chat.ChatController().get_update_message, name='get_update_message'),
    
    # Profile
    url(r'^profile/$', Profile.ProfileController().profile, name='profile'),
    url(r'^profile/update-profile/$', Profile.ProfileController().update_profile, name='update_profile'),
    
    url(r'^logout', User.UserController().logout, name='logout'), 
)