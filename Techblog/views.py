from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from Blog.models import Blog

def index(response):
    template = loader.get_template('Techblog/index.html')
    #instead of doing it by loader we can also do this via render
    return HttpResponse(template.render({},response))

# def sign_up(request):
#     return render(request,'Techblog/login.html')


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            print(form)
            return render(request, 'Techblog/login.html', {'form': form})
    else:
        form = UserCreationForm()
        print(form)
        return render(request, 'Techblog/login.html', {'form': form})


def search(request):
    query = request.GET['query']
    elems = []
    invalid= False
    if len(query) > 70:
        invalid = True
    if not invalid:
        elems = Blog.objects.filter( Q(heading__icontains= query) | Q(content__icontains = query))
        # areit = elems.union(elemsadd)
    return render(request,'Techblog/search.html',{'elems':elems,'query':query,'valid':invalid})
