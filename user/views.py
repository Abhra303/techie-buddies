from django.shortcuts import render,redirect,reverse
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from Blog.models import Comment,Blog

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print('kello')
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            print('no kelo')
            return render(request, 'Techblog/form.html', {'form': form})
    else:
        return render(request, 'Techblog/Signin.html')


def login1(request):
    if request.user.is_authenticated:
        name = request.user.username
        return HttpResponse('Hello ' + name)
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username , password = password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                error_message = 'username or password is incorrect'
                return render(request,'Techblog/login.html',{'error_message':error_message})
        else:
            return render(request,'Techblog/login.html')


def logout1(request):
    logout(request)
    return redirect('/')


def reply(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            comment_text = request.POST['comment']
            parent_id = request.POST['parent']

            comment = Comment.objects.get(pk = parent_id)
            blog = comment.post
            blog_id = blog.pk
            new_rep = Comment(post = blog,user = request.user,parent = comment,body = comment_text)

            new_rep.save()
            return redirect(reverse('Blog:post',args = [blog_id]))
        else:
            return redirect('/')
    else:
        return redirect('/')


