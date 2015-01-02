from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    req_token = models.CharField(max_length=200)
    log = models.CharField(max_length=5)
    
    
class Profile(models.Model):
    user = models.ForeignKey(User)
    display_name = models.CharField(max_length=50)
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
    content = models.CharField(max_length=500)
    agrees = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post)
    user_pic_url = models.CharField(max_length=200)
    user_name = models.CharField(max_length=50)
    comment_date = models.DateTimeField('date published')
    comment = models.CharField(max_length=200)

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
    
# Poll App
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.choice_text