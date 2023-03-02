from django.db import models
from django.contrib.auth.models import User 

import uuid #For unique characters
# Create your models here.
def upload_location_this(instance,filename):
	file_path = 'uploads/{user_id}/{post_id}/this/{file}'.format(user_id=str(instance.user.username),post_id=str(instance.post_id),file=filename)
	return file_path
def upload_location_that(instance,filename):
	file_path = 'uploads/{user_id}/{post_id}/that/{file}'.format(user_id=str(instance.user.username),post_id=str(instance.post_id),file=filename)
	return file_path
class Post(models.Model):
    question             =       models.CharField(max_length=150,null=True)
    post_id              =       models.UUIDField(default=uuid.uuid4, editable=False,unique=True, null=True)
    user                 =       models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    That                 =       models.FileField(upload_to=upload_location_that ,null=True)
    That_text            =       models.CharField(max_length=150,null=True)
    That_filetype        =       models.CharField(max_length=150,null=True)
    That_fileSize        =       models.CharField(max_length=150,null=True)
    That_fileExtension   =       models.CharField(max_length=150,null=True)
    
    This                 =       models.FileField(upload_to=upload_location_this ,null=True)
    This_text            =       models.CharField(max_length=150,null=True)
    This_filetype        =       models.CharField(max_length=150,null=True)
    This_fileSize        =       models.CharField(max_length=150,null=True)
    This_fileExtension   =       models.CharField(max_length=150,null=True)
    
    time            =       models.DateTimeField(auto_now_add=True)
    
    Ip_address      =       models.CharField(max_length=150,null=True, blank=True)
    user_city       =       models.CharField(max_length=150,null=True, blank=True)
    user_country    =       models.CharField(max_length=150,null=True, blank=True)
    user_browser    =       models.CharField(max_length=150,null=True, blank=True)

    def __str__(self):
        return str(self.user.username) + ' --> ' + self.question

class Comment(models.Model):
    comments         =       models.CharField(max_length=1550,null=True)
    user            =       models.ForeignKey(User,on_delete=models.CASCADE,null=True)
   
    comment_id      =       models.UUIDField(default=uuid.uuid4, editable=False,unique=True, null=True)
    root_id         =       models.ForeignKey("self",on_delete=models.CASCADE,null=True,verbose_name="Root_id")
    post            =       models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    deleted         =       models.BooleanField(default=False)
    
    time            =       models.DateTimeField(auto_now_add=True)
    Ip_address      =       models.CharField(max_length=150,null=True, blank=True)
    user_city       =       models.CharField(max_length=150,null=True, blank=True)
    user_country    =       models.CharField(max_length=150,null=True, blank=True)
    user_browser    =       models.CharField(max_length=150,null=True, blank=True)

class Vote(models.Model):
    user            =       models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    post            =       models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    Voted_for       =       models.CharField(max_length=4,null=True, blank=True)    
    
    deleted         =       models.BooleanField(default=False)
    
    time            =       models.DateTimeField(auto_now_add=True)
    Ip_address      =       models.CharField(max_length=150,null=True, blank=True)
    user_city       =       models.CharField(max_length=150,null=True, blank=True)
    user_country    =       models.CharField(max_length=150,null=True, blank=True)
    user_browser    =       models.CharField(max_length=150,null=True, blank=True)


