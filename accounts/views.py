from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User ,auth

# Create your views here.


def get_user_view(request):
    
    #user =  get_object_or_404(User, email=request.user)

    return render(request,'accounts/view.html')


def login(request):
    redirect_to = request.GET.get('next', '')
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']
        
        message=''

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            message ="logged in  successful"
            messages.info(request,message)
            return redirect(redirect_to)
        else:
            message ="Invalid username or password"
            return render(request,'accounts/login.html',{'error': message})
    else:
        return render(request,'accounts/login.html',{'redirect_to':redirect_to})

def register(request):

    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['C-password']
        message = ''
        if password == Cpassword:
            if User.objects.filter(username=username).exists():
                message ="Username already exist"
            elif User.objects.filter(email=email).exists():
                message ="Email already exist"
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                #user.save()
                message ="Registeration successful"
                messages.info(request,message)
                return redirect('/accounts/')
        else:
            message ="Password not matching...."
        return render(request,'accounts/register.html',{'error': message})
    else:
        return render(request,'accounts/register.html')

def logout(request):
    try:
        auth.logout(request)
        message ="Successfully logged out"
        messages.info(request,message)
        return redirect('/accounts/')
    except:
        message ="Sorry Something went wrong"
        messages.info(request,message)
        return redirect('accounts/')