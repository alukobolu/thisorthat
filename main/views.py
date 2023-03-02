from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from .models import Post,Comment,Vote
from .forms import PostForm


def posting(request):
    if request.user.is_authenticated ==True:
        if request.method =='POST':
            question = request.POST["question"]
            type = request.POST['type']
            if type !='text' :
                form  = PostForm(request.POST,request.FILES)
                if form.is_valid():

                    instance = Post()
                    instance.question           = question
                    instance.user               = request.user

                    this = request.FILES.get('this')
                    that = request.FILES.get('that')
                    instance.This               = this
                    instance.This_fileSize      = this.size
                    instance.This_fileExtension      = str(this).split('.')[-1]
                    instance.This_filetype           = this.content_type
                    
                    instance.That               = that
                    instance.That_fileSize      = that.size
                    instance.That_fileExtension      = str(that).split('.')[-1]
                    instance.That_filetype           = that.content_type
                    instance.save()
                   
                    message ="Post successful"
                    messages.info(request,message)
                    return HttpResponseRedirect('/accounts/' )
                print('problem')
            else:
                this = request.POST['this']
                that = request.POST['that']

                instance = Post()
                instance.question           = question
                instance.user               = request.user

                instance.This_text          = this
                instance.That_text          = that

                instance.This_filetype      = "text"
                instance.That_filetype      = "text"
                instance.save()
                
            message ="Post successful"
            messages.info(request,message)
            return HttpResponseRedirect('/accounts/' )
        else:
            a_post = Post.objects.all()
            return render(request,'main/post-page.html',{'post':a_post})       
    else:
        return HttpResponseRedirect('/accounts/login/?next='+request.path )


def view_post(request,id):
    if request.method =='GET':
        try:
            a_post = Post.objects.get(post_id=id)
            comments = Comment.objects.filter(post=a_post)
            return render(request,'main/main.html',{'post':a_post,'comments':comments})
        except:
            message ="This Post does not exist"
            messages.info(request,message)
            return render(request,'error/404.html')

def voting(request):
    if request.method == "POST":
        try:
            voted_for = request.POST['voted_for']
            post_id   = request.POST['post_id']      
            post = Post.objects.get(post_id = post_id)

            instance = Vote()
            instance.post = post    
            instance.Voted_for = voted_for

            if request.user.is_authenticated ==True:
                instance.user = request.user
            instance.save()
            return render(request,'main/main.html')
        except:
            message ="This Post does not exist"
            messages.info(request,message)
            return render(request,'error/404.html')

def commenting(request):
    if request.method == "POST":
        try:
            comment = request.POST['comment']
            post_id   = request.POST['post_id']   
            root_comment_id = request.POST['comment_id']
            post = Post.objects.get(post_id = post_id)

            instance = Comment()
            instance.comments = comment
            instance.post = post
            
            if root_comment_id != '0':
                root = Comment.objects.get(comment_id=root_comment_id)
                instance.root_id = root
            if request.user.is_authenticated ==True:
                    instance.user = request.user
            instance.save()
            return render(request,'main/main.html')
        except:
            message ="This Post does not exist"
            messages.info(request,message)
            return render(request,'error/404.html')
