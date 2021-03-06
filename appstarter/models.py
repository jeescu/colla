from django.db import models
from datetime import datetime
from appstarter import config
import os
import uuid


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    fullname = models.CharField(max_length=100)
    provider_user_id = models.CharField(max_length=200, null=True)

    def profile(self):
        return Profile.objects.get(user=self.id)


class Authentication(models.Model):
    user_id = models.IntegerField(default=0)
    provider = models.CharField(max_length=50, null=True)
    provider_user_id = models.CharField(max_length=200, null=True)
    access_token = models.CharField(max_length=1000)
    expired_at = models.DateTimeField('expired_date')


class Profile(models.Model):
    user = models.ForeignKey(User)
    dis_name = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=200)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    mail_address = models.CharField(max_length=30)


class Post(models.Model):
    user = models.ForeignKey(User)
    share_type = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    title = models.CharField(max_length=50)
    content_text = models.CharField(max_length=5000)
    content_image = models.CharField(max_length=200)
    content_link = models.CharField(max_length=500)
    agrees = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def comment(self):
        return Comment.objects.filter(post=self.id)
    
    def agreed(self):
        return Agree.objects.filter(post=self.id)


class Agree(models.Model):
    post = models.ForeignKey(Post)
    user_name = models.CharField(max_length=50) 


class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    comment_date = models.DateTimeField(default=datetime.now())
    comment = models.CharField(max_length=500)


# Developers article
class Article(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=800)
    cover = models.CharField(max_length=200)
    date = models.DateTimeField('date published')


class Board(models.Model):
    board_name = models.CharField(max_length=50)
    board_description = models.CharField(max_length=200)


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_color = models.CharField(max_length=50)


class Forum(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length=500)
    detail = models.CharField(max_length=1000)
    mark_answered = models.IntegerField(default=0)


class ForumTag(models.Model):
    forum = models.ForeignKey(Forum)
    tag = models.ForeignKey(Tag)


class ForumComments(models.Model):
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=2000)
    mark_resolved = models.IntegerField(default=0)


class Issue(models.Model):
    user = models.ForeignKey(User)
    detail = models.CharField(max_length=1000)
    issue_type = models.CharField(max_length=50)
    error_message = models.CharField(max_length=1500)
    code_preview = models.CharField(max_length=1000)


class IssueComments(models.Model):
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=2000)


class BoardIssue(models.Model):
    board = models.ForeignKey(Board)
    issue = models.ForeignKey(Issue)


class Resources(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)


# Messenger
class Chat(models.Model):
    date_activated = models.DateTimeField('date published')


# chat.chatuser_set.create(user_id = 1)
class ChatUser(models.Model):
    chat = models.ForeignKey(Chat)
    user_id = models.IntegerField(default=0)


# ChatMessage.objects.filter(chat = chat.id).order_by('date_sent')
# chat.chatmessage_set.create(user_id=1, message="Hello")    
class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat)
    user_id = models.IntegerField(default=0)
    message = models.CharField(max_length=500)
    date_sent = models.DateTimeField('date sent')
        
    def profile(self):
        return Profile.Objects.filter(user=self.user_id)


# Groups - A private Collaboration for teams (Page Spec)
class Group(models.Model):
    group_name = models.CharField(max_length=50)
    group_detail = models.CharField(max_length=300)
    group_created = models.DateTimeField('date published')
    group_pic = models.CharField(max_length=200)
    group_users = models.IntegerField(default=0)


class GroupUser(models.Model):
    group = models.ForeignKey(Post)
    group_joined_user_id = models.IntegerField(default=0)
    group_joined_date = models.DateTimeField('date published')


# @WATCHME: Path from environment
def gen_post_file_name(instance, filename):
    path = config.post_image_upload_path
    f, ext = os.path.splitext(filename)
    return path+'%s%s' % (uuid.uuid4().hex, ext)


def gen_profile_file_name(instance, filename):
    path = config.profile_image_upload_path
    f, ext = os.path.splitext(filename)
    return path+'%s%s' % (uuid.uuid4().hex, ext)


class PostImage(models.Model):
    post_image = models.ImageField(upload_to=gen_post_file_name)


class ProfileImage(models.Model):
    profile_image = models.ImageField(upload_to=gen_profile_file_name)
