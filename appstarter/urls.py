from django.conf.urls import patterns, url
from appstarter.controller import UserController, PostController, ProfileController, AuthController, ChatController, ArticleController

user = UserController.UserController()
auth = AuthController.AuthController()
post = PostController.PostController()
chat = ChatController.ChatController()
profile = ProfileController.ProfileController()
article = ArticleController.ArticleController()

urlpatterns = patterns('',
    # user
    url(r'^$', user.login, name='index'),
    url(r'^signup/$', user.register, name='signup'),
    url(r'^register/', user.do_register, name='register'),
    url(r'^dashboard/$', user.index, name='home'),
    url(r'^logout', user.logout, name='logout'),
    
    # social login
    url(r'^login/facebook/$', auth.facebook_login, name='facebook_login'),
    url(r'^login/google/$', auth.google_login, name='google_login'),
                       
    # Post
    url(r'^new-post/$', post.add_post, name='new_post'),
    url(r'^update-post/$', post.get_new_post, name='update_post'),
    url(r'^more-post/$', post.get_more_post, name='more_post'),
                     
    # Agree and Comment                   
    url(r'^new-comment/$', post.comment_post, name='new_comment'),
    url(r'^new-agree/$', post.agree_post, name='agree_post'),

    # Article
    url(r'^get-article/$', article.get, name='get_article'),
    url(r'^new-article/$', article.create, name='new_article'),
    url(r'^update-article/$', article.update, name='update_article'),
    
    # Chat                   
    url(r'^new-message/$', chat.new_message, name='new_message'),
    url(r'^get-messages/$', chat.get_message, name='get_message'),
    url(r'^get-update-messages/$', chat.get_update_message, name='get_update_message'),
    
    # Profile
    url(r'^profile/$', profile.profile, name='profile'),
    url(r'^profile/update-profile/$', profile.update_profile, name='update_profile'),
)
