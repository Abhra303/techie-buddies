from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

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
